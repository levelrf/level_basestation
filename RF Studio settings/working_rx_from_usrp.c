// Rf settings for CC1101
RF_SETTINGS code rfSettings = {
    0x06,  // IOCFG0          GDO0 Output Pin Configuration
    0x05,  // PKTCTRL0        Packet Automation Control
    0x06,  // FSCTRL1         Frequency Synthesizer Control
    0x21,  // FREQ2           Frequency Control Word, High Byte
    0x62,  // FREQ1           Frequency Control Word, Middle Byte
    0x76,  // FREQ0           Frequency Control Word, Low Byte
    0x2B,  // MDMCFG4         Modem Configuration
    0x3B,  // MDMCFG3         Modem Configuration
    0x75,  // MDMCFG2         Modem Configuration
    0x15,  // DEVIATN         Modem Deviation Setting
    0x18,  // MCSM0           Main Radio Control State Machine Configuration
    0x16,  // FOCCFG          Frequency Offset Compensation Configuration
    0xFB,  // WORCTRL         Wake On Radio Control
    0xEA,  // FSCAL3          Frequency Synthesizer Calibration
    0x2A,  // FSCAL2          Frequency Synthesizer Calibration
    0x00,  // FSCAL1          Frequency Synthesizer Calibration
    0x1F,  // FSCAL0          Frequency Synthesizer Calibration
    0x09,  // TEST0           Various Test Settings
    0xFF,  // LQI             Demodulator Estimate for Link Quality
    0x80,  // RSSI            Received Signal Strength Indication
    0x01,  // MARCSTATE       Main Radio Control State Machine State
    0x80,  // PKTSTATUS       Current GDOx Status and Packet Status
    0x94,  // VCO_VC_DAC      Current Setting from PLL Calibration Module
};