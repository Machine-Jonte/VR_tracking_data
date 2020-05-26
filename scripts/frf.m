clear

% T_left = readtable('./computer_generated_paths/sweepsine/sweepsineleft.csv', 'HeaderLines', 1);
% T_right = readtable('./computer_generated_paths/sweepsine/sweepsineright.csv', 'HeaderLines', 1);
T_left = readtable('../IKFast/computer_generated/sweepsine/sweepsine_left.csv', 'HeaderLines', 1);
T_right = readtable('../IKFast/computer_generated/sweepsine/sweepsine_right.csv', 'HeaderLines', 1);

input_signal = table2array( T_right(:,3) );
output_signal = table2array( T_right(:,6) );

input_signal = reshape(input_signal, 1, []);
output_signal = reshape(output_signal, 1, []);

data=iddata(output_signal,input_signal,0.1);

% h = fir1(30,0.2,rectwin(31));
% x = randn(16384,1);
% y = filter(h,1,x);


% fs = 500;
% tfestimate(x,y,1024,[],[],fs)
% sys = tfest(data, 2)

fs = 10;
tfestimate(input_signal, output_signal, 1024,[],[],fs)
% bode(sys)
