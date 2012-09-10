%Octave script to convert binary file that GNU Radio captures to a text file so we can search and grep through it more easily

%unlink(rx.txt); %delete existing text file
fid = fopen('/home/hunter/rx.dat', 'r'); %read in file from gnuradio
if(!fid)
	fprint("Could not open file\n");
endif

[data count] = fread(fid);
data = data'; %transpose to row vector
printf("Found preamble at the following places: ")
positions = findstr(data, [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1  1 0 1 0 1 0 1 0])
%positions = findstr(data, [0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1])
for i = 1:length(positions)
	printf("Match: ")
	binary = data(positions(i):(positions(i)+200));
	%need to convert that vector of binary into a string of binary
	%bstring = "";
	%for j = 1:length(binary)
	%	bstring = strcat(binary, binary(j))
	%end
	binary = mat2str(binary);
	binary = strrep(binary, ",","");
	binary = strrep(binary, "[","");
	binary = strrep(binary, "]","");
	hex = bin2dec(binary);
	hex = dec2hex(hex)
end

fid = fclose(fid);
if(fid)
	fprint("Could not close file\n");
endif

