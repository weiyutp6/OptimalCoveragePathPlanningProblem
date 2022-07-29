//#include "LKH.h"
#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>

#include "../SRC/Distance.c"
#include "../SRC/IsCandidate.c"
#include "../SRC/PrintParameters.c"
#include "../SRC/ReadLine.c"
#include "../SRC/ReadPenalties.c"
#include "../SRC/SolveGTSP.c"
#include "../SRC/Statistics.c"
#include "../SRC/eprintf.c"
#include "../SRC/printff.c"
#include "../SRC/Distance_SPECIAL.c"
#include "../SRC/GetTime.c"
#include "../SRC/PostOptimize.c"
#include "../SRC/Random.c"
#include "../SRC/ReadParameters.c"
#include "../SRC/ReadProblem.c"
#include "../SRC/SolveTSP.c"
#include "../SRC/WriteTour.c"
#include "../SRC/fscanint.c"

GainType SolveGTSP(int *GTour);
GainType PostOptimize(int *GTour, GainType Cost);
static double GetTimeUsage(int who);

/*
 * This file contains the main function of the program.
 */

int main(int argc, char *argv[])
{
    int Exp, Experiments = 10;
    GainType Cost, CostSum = 0;
    int *GTour, RunSum = 0, Opt = 0;
    double Time = 0;

    /* Read the specification of the problem */
    if (argc >= 2) {
        ParameterFileName = argv[1];
        if (argc >= 3)
            Experiments = atoi(argv[2]);
    }
    ReadParameters();
    ReadProblem();
    assert(GTour = (int *) malloc((GTSPSets + 1) * sizeof(int)));
    for (Exp = 1; Exp <= Experiments; Exp++, Seed++) {
        Cost = SolveGTSP(GTour);
        RunSum += Run;
        Cost = PostOptimize(GTour, Cost);
        if (OutputTourFileName) {
            int OldTraceLevel = TraceLevel, OldDimension = Dimension;
            TraceLevel = 1;
            Dimension = ProblemType != ATSP ? GTSPSets : 2 * GTSPSets;
            WriteTour(OutputTourFileName, GTour, Cost);
            TraceLevel = OldTraceLevel;
            Dimension = OldDimension;
        }
        if (TourFileName && (Optimum == MINUS_INFINITY || Cost < Optimum)) {
            int OldTraceLevel = TraceLevel, OldDimension = Dimension;
            TraceLevel = 1;
            Dimension = ProblemType != ATSP ? GTSPSets : 2 * GTSPSets;
            WriteTour(TourFileName, GTour, Cost);
            TraceLevel = OldTraceLevel;
            Dimension = OldDimension;
        }
        if (TraceLevel > 0)
            printff("* Performed %d out of %d experiments\n\n",
                    Exp, Experiments);
        CostSum += Cost;
        if (Cost == Optimum)
            Opt++;
        else if (Cost < Optimum) {
            Optimum = Cost;
            Opt = 1;
        }
    }
    Time = GetTimeUsage(RUSAGE_SELF) + GetTimeUsage(RUSAGE_CHILDREN);
    printff
        ("Opt = " GainFormat ", Value = %0.1f, Error = %0.2f%%\n"
         "Opt = %0.0f%%, Time = %0.1fs, Runs = %0.1f\n\n",
         Optimum, (double) CostSum / Experiments,
         ((double) CostSum / Experiments - Optimum) / Optimum * 100.0,
         Opt * 100.0 / Experiments, Time / Experiments,
         (double) RunSum / Experiments);
    return 0;
}

static double GetTimeUsage(int who)
{
    struct rusage ru;
    getrusage(who, &ru);
    return ru.ru_utime.tv_sec + ru.ru_utime.tv_usec / 1000000.0;
}
