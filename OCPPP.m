% load NAI matrix from python generated NAI.mat
NAIs = load("NAI.mat");
Ah = NAIs.NAIH;
Ah = cast(Ah, "double");
Av = NAIs.NAIV;
Av = cast(Av, "double");
a = size(Ah);

% optimization variables
xh = optimvar('xh',a(2),'Type','integer','LowerBound',0,'UpperBound',1);
xv = optimvar('xv',a(2),'Type','integer','LowerBound',0,'UpperBound',1);
yh = optimvar('yh',a(1),'Type','integer','LowerBound',0,'UpperBound',1);
yv = optimvar('yv',a(1),'Type','integer','LowerBound',0,'UpperBound',1);

% LP formulation
% min   1'*yh + 1'*yv
% s.t.  Ah*xh <= yh,
%       Av*xv <= yv,
%       xh + xv = 1,
%       xh, xv \in {0,1}^n
obj = h(xh,xv,yh,yv);
prob = optimproblem('Objective', obj);
ineq_xh = Ah*xh<=yh;
ineq_xv = Av*xv<=yv;
eq_x = xh + xv == ones(a(2),1);
prob.Constraints.ineq1 = ineq_xh;
prob.Constraints.ineq2 = ineq_xv;
prob.Constraints.eq_x = eq_x;

% solver
sol = solve(prob);
sol.xh;
sol.xv;
sol.yh;
sol.yv;
writematrix(sol.xh, 'xh.csv')

% cost function
function h = h(xh, xv, yh, yv)
    h = sum(yh, 'all') + sum(yv, 'all');
end