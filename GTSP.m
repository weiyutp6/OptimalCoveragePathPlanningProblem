tsp_cost = load("tsp_cost.mat");
C = cast(tsp_cost.tsp_cost,"double");
c = size(C);
global C

X = optimvar('X', c(1), c(2),'Type','integer','LowerBound', 0,'UpperBound', 1);
u = optimvar('u', c(1), 2, 'Type', 'integer', 'LowerBound', 1, 'UpperBound', c(1));

obj = h(X);
prob = optimproblem('Objective', obj);
ineq_row = X*ones(c(1),1) >= ones(c(1),1);
ineq_column = X'*ones(c(2),1) >= zeros(c(2),1);
prob.Constraints.ineq1 = ineq_row;
prob.Constraints.ineq2 = ineq_column;

sol = solve(prob);
sol.X;
writematrix(sol.X, 'GTSP_result.csv');

function h = h(x)
    global C
    h = sum(C.*x ,'all');
end