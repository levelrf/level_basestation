/* -*- c++ -*- */
/*
 * Copyright 2008,2009,2010,2011 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef FREQUENCY_DISPLAY_PLOT_C
#define FREQUENCY_DISPLAY_PLOT_C

#include <FrequencyDisplayPlot.h>

#include "qtgui_types.h"
#include <qwt_scale_draw.h>
#include <qwt_legend.h>
#include <qwt_legend_item.h>
#include <QColor>
#include <iostream>

/***********************************************************************
 * Widget to provide mouse pointer coordinate text
 **********************************************************************/
class FreqDisplayZoomer: public QwtPlotZoomer, public FreqOffsetAndPrecisionClass
{
public:
  FreqDisplayZoomer(QwtPlotCanvas* canvas, const unsigned int freqPrecision)
    : QwtPlotZoomer(canvas),
      FreqOffsetAndPrecisionClass(freqPrecision)
  {
    setTrackerMode(QwtPicker::AlwaysOn);
  }
  
  virtual void updateTrackerText()
  {
    updateDisplay();
  }

  void SetUnitType(const std::string &type)
  {
    _unitType = type;
  }

protected:
  using QwtPlotZoomer::trackerText;
  virtual QwtText trackerText(QPoint const &p) const
  {
    QwtDoublePoint dp = QwtPlotZoomer::invTransform(p);
    QwtText t(QString("%1 %2, %3 dB")
              .arg(dp.x(), 0, 'f', GetFrequencyPrecision())
	          .arg(_unitType.c_str()).arg(dp.y(), 0, 'f', 2));
    return t;
  }

private:
  std::string _unitType;
};


/***********************************************************************
 * Main frequency display plotter widget
 **********************************************************************/
FrequencyDisplayPlot::FrequencyDisplayPlot(int nplots, QWidget* parent)
  : DisplayPlot(nplots, parent)
{
  _startFrequency = 0;
  _stopFrequency = 4000;

  _useCenterFrequencyFlag = false;

  _numPoints = 1024;
  _minFFTPoints = new double[_numPoints];
  _maxFFTPoints = new double[_numPoints];
  _xAxisPoints = new double[_numPoints];

  setAxisTitle(QwtPlot::xBottom, "Frequency (Hz)");
  setAxisScaleDraw(QwtPlot::xBottom, new FreqDisplayScaleDraw(0));

  _minYAxis = -120;
  _maxYAxis = 10;
  setAxisScaleEngine(QwtPlot::yLeft, new QwtLinearScaleEngine);
  setAxisScale(QwtPlot::yLeft, _minYAxis, _maxYAxis);
  setAxisTitle(QwtPlot::yLeft, "Power (dB)");

  QList<QColor> colors;
  colors << QColor(Qt::yellow) << QColor(Qt::red) << QColor(Qt::green)
	 << QColor(Qt::black) << QColor(Qt::cyan) << QColor(Qt::magenta)
	 << QColor(Qt::blue) << QColor(Qt::gray) << QColor(Qt::darkRed)
	 << QColor(Qt::darkGreen) << QColor(Qt::darkBlue) << QColor(Qt::darkGray);

  // Automatically deleted when parent is deleted
  for(int i = 0; i < _nplots; i++) {
    _dataPoints.push_back(new double[_numPoints]);
    memset(_dataPoints[i], 0x0, _numPoints*sizeof(double));

    _plot_curve.push_back(new QwtPlotCurve(QString("Data %1").arg(i)));
    _plot_curve[i]->attach(this);
    _plot_curve[i]->setPen(QPen(colors[i]));
    
    const QwtSymbol *symbol = new QwtSymbol(QwtSymbol::NoSymbol, QBrush(colors[i]), QPen(colors[i]), QSize(7,7));
    
#if QWT_VERSION < 0x060000
    _plot_curve[i]->setRawData(_xAxisPoints, _dataPoints[i], _numPoints);
    _plot_curve[i]->setSymbol(*symbol);
#else
    _plot_curve[i]->setRawSamples(_xAxisPoints, _dataPoints[i], _numPoints);
    _plot_curve[i]->setSymbol(symbol);
#endif
  }

  _min_fft_plot_curve = new QwtPlotCurve("Minimum Power");
  _min_fft_plot_curve->attach(this);
  _min_fft_plot_curve->setPen(QPen(Qt::magenta));

#if QWT_VERSION < 0x060000
  _min_fft_plot_curve->setRawData(_xAxisPoints, _minFFTPoints, _numPoints);
#else
  _min_fft_plot_curve->setRawSamples(_xAxisPoints, _minFFTPoints, _numPoints);
#endif

  _min_fft_plot_curve->setVisible(false);

  _max_fft_plot_curve = new QwtPlotCurve("Maximum Power");
  _max_fft_plot_curve->attach(this);
  _max_fft_plot_curve->setPen(QPen(Qt::darkYellow));

#if QWT_VERSION < 0x060000
  _max_fft_plot_curve->setRawData(_xAxisPoints, _maxFFTPoints, _numPoints);
#else
  _max_fft_plot_curve->setRawSamples(_xAxisPoints, _maxFFTPoints, _numPoints);
#endif

  _max_fft_plot_curve->setVisible(false);

  _lower_intensity_marker= new QwtPlotMarker();
  _lower_intensity_marker->setLineStyle(QwtPlotMarker::HLine);
  _lower_intensity_marker->setLinePen(QPen(Qt::cyan));
  _lower_intensity_marker->attach(this);

  _upper_intensity_marker = new QwtPlotMarker();
  _upper_intensity_marker->setLineStyle(QwtPlotMarker::HLine);
  _upper_intensity_marker->setLinePen(QPen(Qt::green, 0, Qt::DotLine));
  _upper_intensity_marker->attach(this);

  memset(_xAxisPoints, 0x0, _numPoints*sizeof(double));

  for(int64_t number = 0; number < _numPoints; number++){
    _minFFTPoints[number] = 200.0;
    _maxFFTPoints[number] = -280.0;
  }

  // set up peak marker
  QwtSymbol symbol;

  _markerPeakAmplitude = new QwtPlotMarker();
  _markerPeakAmplitude->setLinePen(QPen(Qt::yellow));
  symbol.setStyle(QwtSymbol::Diamond);
  symbol.setSize(8);
  symbol.setPen(QPen(Qt::yellow));
  symbol.setBrush(QBrush(Qt::yellow));

#if QWT_VERSION < 0x060000
  _markerPeakAmplitude->setSymbol(symbol);
#else
  _markerPeakAmplitude->setSymbol(&symbol);
#endif

  /// THIS CAUSES A PROBLEM!
  //_markerPeakAmplitude->attach(this);

  _markerNoiseFloorAmplitude = new QwtPlotMarker();
  _markerNoiseFloorAmplitude->setLineStyle(QwtPlotMarker::HLine);
  _markerNoiseFloorAmplitude->setLinePen(QPen(Qt::darkRed, 0, Qt::DotLine));
  _markerNoiseFloorAmplitude->attach(this);

  _markerCF= new QwtPlotMarker();
  _markerCF->setLineStyle(QwtPlotMarker::VLine);
  _markerCF->setLinePen(QPen(Qt::lightGray, 0, Qt::DotLine));
  _markerCF->attach(this);
  _markerCF->hide();

  _peakFrequency = 0;
  _peakAmplitude = -HUGE_VAL;

  _noiseFloorAmplitude = -HUGE_VAL;

  replot();

  _zoomer = new FreqDisplayZoomer(canvas(), 0);

#if QWT_VERSION < 0x060000
  _zoomer->setSelectionFlags(QwtPicker::RectSelection | QwtPicker::DragSelection);
#endif

  _zoomer->setMousePattern(QwtEventPattern::MouseSelect2,
			  Qt::RightButton, Qt::ControlModifier);
  _zoomer->setMousePattern(QwtEventPattern::MouseSelect3,
			  Qt::RightButton);


  const QColor c(Qt::darkRed);
  _zoomer->setRubberBandPen(c);
  _zoomer->setTrackerPen(c);

  // Do this after the zoomer has been built
  _resetXAxisPoints();

  // Turn off min/max hold plots in legend
  QWidget *w;
  QwtLegend* legendDisplay = legend();
  w = legendDisplay->find(_min_fft_plot_curve);
  ((QwtLegendItem*)w)->setChecked(true);
  w = legendDisplay->find(_max_fft_plot_curve);
  ((QwtLegendItem*)w)->setChecked(true);
}

FrequencyDisplayPlot::~FrequencyDisplayPlot()
{
  for(int i = 0; i < _nplots; i++)
    delete [] _dataPoints[i];

  delete[] _maxFFTPoints;
  delete[] _minFFTPoints;
  delete[] _xAxisPoints;
}

void
FrequencyDisplayPlot::set_yaxis(double min, double max)
{
  // Get the new max/min values for the plot
  _minYAxis = min;
  _maxYAxis = max;

  // Set the axis max/min to the new values
  setAxisScale(QwtPlot::yLeft, _minYAxis, _maxYAxis);

  // Reset the base zoom level to the new axis scale set here
  _zoomer->setZoomBase();
}

void
FrequencyDisplayPlot::SetFrequencyRange(const double constStartFreq,
					const double constStopFreq,
					const double constCenterFreq,
					const bool useCenterFrequencyFlag,
					const double units, const std::string &strunits)
{
  double startFreq = constStartFreq / units;
  double stopFreq = constStopFreq / units;
  double centerFreq = constCenterFreq / units;

  _xAxisMultiplier = units;
  _useCenterFrequencyFlag = useCenterFrequencyFlag;

  if(_useCenterFrequencyFlag){
    startFreq = (startFreq + centerFreq);
    stopFreq = (stopFreq + centerFreq);
  }

  bool reset = false;
  if((startFreq != _startFrequency) || (stopFreq != _stopFrequency))
    reset = true;

  if(stopFreq > startFreq) {
    _startFrequency = startFreq;
    _stopFrequency = stopFreq;

    if((axisScaleDraw(QwtPlot::xBottom) != NULL) && (_zoomer != NULL)){
      double display_units = ceil(log10(units)/2.0);
      setAxisScaleDraw(QwtPlot::xBottom, new FreqDisplayScaleDraw(display_units));
      setAxisTitle(QwtPlot::xBottom, QString("Frequency (%1)").arg(strunits.c_str()));

      if(reset)
	_resetXAxisPoints();

      ((FreqDisplayZoomer*)_zoomer)->SetFrequencyPrecision(display_units);
      ((FreqDisplayZoomer*)_zoomer)->SetUnitType(strunits);
    }
  }
}


double
FrequencyDisplayPlot::GetStartFrequency() const
{
  return _startFrequency;
}

double
FrequencyDisplayPlot::GetStopFrequency() const
{
  return _stopFrequency;
}

void
FrequencyDisplayPlot::replot()
{
  _markerNoiseFloorAmplitude->setYValue(_noiseFloorAmplitude);

  // Make sure to take into account the start frequency
  if(_useCenterFrequencyFlag){
    _markerPeakAmplitude->setXValue((_peakFrequency/1000.0) + _startFrequency);
  }
  else{
    _markerPeakAmplitude->setXValue(_peakFrequency + _startFrequency);
  }
  _markerPeakAmplitude->setYValue(_peakAmplitude);

  QwtPlot::replot();
}

void
FrequencyDisplayPlot::PlotNewData(const std::vector<double*> dataPoints,
				  const int64_t numDataPoints,
				  const double noiseFloorAmplitude, const double peakFrequency,
				  const double peakAmplitude, const double timeInterval)
{
  if(!_stop) {
    if(numDataPoints > 0) {
      if(numDataPoints != _numPoints) {
	_numPoints = numDataPoints;

	delete[] _minFFTPoints;
	delete[] _maxFFTPoints;
	delete[] _xAxisPoints;
	_xAxisPoints = new double[_numPoints];
	_minFFTPoints = new double[_numPoints];
	_maxFFTPoints = new double[_numPoints];

	for(int i = 0; i < _nplots; i++) {
	  delete[] _dataPoints[i];
	  _dataPoints[i] = new double[_numPoints];

#if QWT_VERSION < 0x060000
	  _plot_curve[i]->setRawData(_xAxisPoints, _dataPoints[i], _numPoints);
	  _min_fft_plot_curve->setRawData(_xAxisPoints, _minFFTPoints, _numPoints);
	  _max_fft_plot_curve->setRawData(_xAxisPoints, _maxFFTPoints, _numPoints);
#else
	  _plot_curve[i]->setRawSamples(_xAxisPoints, _dataPoints[i], _numPoints);
	  _min_fft_plot_curve->setRawSamples(_xAxisPoints, _minFFTPoints, _numPoints);
	  _max_fft_plot_curve->setRawSamples(_xAxisPoints, _maxFFTPoints, _numPoints);
#endif
	}

	_resetXAxisPoints();
	ClearMaxData();
	ClearMinData();
      }

      for(int i = 0; i < _nplots; i++) {
	memcpy(_dataPoints[i], dataPoints[i], numDataPoints*sizeof(double));
      }

      for(int64_t point = 0; point < numDataPoints; point++){
	if(dataPoints[0][point] < _minFFTPoints[point]) {
	  _minFFTPoints[point] = dataPoints[0][point];
	}
	if(dataPoints[0][point] > _maxFFTPoints[point]) {
	  _maxFFTPoints[point] = dataPoints[0][point];
	}
      }

      _noiseFloorAmplitude = noiseFloorAmplitude;
      _peakFrequency = peakFrequency;
      _peakAmplitude = peakAmplitude;

      SetUpperIntensityLevel(_peakAmplitude);

      replot();
    }
  }
}

void
FrequencyDisplayPlot::PlotNewData(const double* dataPoints,
				  const int64_t numDataPoints,
				  const double noiseFloorAmplitude, const double peakFrequency,
				  const double peakAmplitude, const double timeInterval)
{
  std::vector<double*> vecDataPoints;
  vecDataPoints.push_back((double*)dataPoints);
  PlotNewData(vecDataPoints, numDataPoints, noiseFloorAmplitude,
	      peakFrequency, peakAmplitude, timeInterval);
}

void
FrequencyDisplayPlot::ClearMaxData()
{
  for(int64_t number = 0; number < _numPoints; number++) {
    _maxFFTPoints[number] = _minYAxis;
  }
}

void
FrequencyDisplayPlot::ClearMinData()
{
  for(int64_t number = 0; number < _numPoints; number++) {
    _minFFTPoints[number] = _maxYAxis;
  }
}

void
FrequencyDisplayPlot::SetMaxFFTVisible(const bool visibleFlag)
{
  _max_fft_plot_curve->setVisible(visibleFlag);
}

void
FrequencyDisplayPlot::SetMinFFTVisible(const bool visibleFlag)
{
  _min_fft_plot_curve->setVisible(visibleFlag);
}

void
FrequencyDisplayPlot::_resetXAxisPoints()
{
  double fft_bin_size = (_stopFrequency-_startFrequency)
    / static_cast<double>(_numPoints);
  double freqValue = _startFrequency;
  for(int64_t loc = 0; loc < _numPoints; loc++) {
    _xAxisPoints[loc] = freqValue;
    freqValue += fft_bin_size;
  }

  setAxisScale(QwtPlot::xBottom, _startFrequency, _stopFrequency);

  // Set up zoomer base for maximum unzoom x-axis
  // and reset to maximum unzoom level
  QwtDoubleRect zbase = _zoomer->zoomBase();
  zbase.setLeft(_startFrequency);
  zbase.setRight(_stopFrequency);
  _zoomer->zoom(zbase);
  _zoomer->setZoomBase(zbase);
  _zoomer->zoom(0);
}

void
FrequencyDisplayPlot::SetLowerIntensityLevel(const double lowerIntensityLevel)
{
  _lower_intensity_marker->setYValue(lowerIntensityLevel);
}

void
FrequencyDisplayPlot::SetUpperIntensityLevel(const double upperIntensityLevel)
{
  _upper_intensity_marker->setYValue(upperIntensityLevel);
}

void
FrequencyDisplayPlot::SetTraceColour(QColor c)
{
  _plot_curve[0]->setPen(QPen(c));
}

void
FrequencyDisplayPlot::SetBGColour(QColor c)
{
  QPalette palette;
  palette.setColor(canvas()->backgroundRole(), c);
  canvas()->setPalette(palette);
}

void
FrequencyDisplayPlot::ShowCFMarker(const bool show)
{
  if (show)
    _markerCF->show();
  else
    _markerCF->hide();
}


void
FrequencyDisplayPlot::OnPickerPointSelected(const QwtDoublePoint & p)
{
  QPointF point = p;
  //fprintf(stderr,"OnPickerPointSelected %f %f %d\n", point.x(), point.y(), _xAxisMultiplier);
  point.setX(point.x() * _xAxisMultiplier);
  emit plotPointSelected(point);
}

void
FrequencyDisplayPlot::OnPickerPointSelected6(const QPointF & p)
{
  QPointF point = p;
  //fprintf(stderr,"OnPickerPointSelected %f %f %d\n", point.x(), point.y(), _xAxisMultiplier);
  point.setX(point.x() * _xAxisMultiplier);
  emit plotPointSelected(point);
}

#endif /* FREQUENCY_DISPLAY_PLOT_C */
