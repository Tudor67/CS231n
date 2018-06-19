%% x(:, i) -> neuron's output for digit i-1
a = 0.99;
b = 1;
x = (a + (b - a) * rand(10)) .* eye(10); 
x = x + (0.01 * rand(10)) .* ~eye(10);

%% weights and biases
w = [0 0 0 0 0 0 0 0 1 1;
     0 0 0 0 1 1 1 1 0 0;
     0 0 1 1 0 0 1 1 0 0;
     0 1 0 1 0 1 0 1 0 1];
b = -0.98;

%% output
output = heaviside(w * x + b);

%% disp
disp(x);
disp(output);