import FWCore.ParameterSet.Config as cms
from DQMOffline.L1Trigger import L1TTauOffline_cfi
import six

variables = {
    'tau': L1TTauOffline_cfi.tauEfficiencyThresholds,
    'NonIsotau': L1TTauOffline_cfi.tauEfficiencyThresholds,
}

plots = {
    'tau': [
        "efficiencyIsoTauET_EB", "efficiencyIsoTauET_EE",
        "efficiencyIsoTauET_EB_EE"
    ],
    'NonIsotau' : [
        "efficiencyNonIsoTauET_EB", "efficiencyNonIsoTauET_EE",
        "efficiencyNonIsoTauET_EB_EE"
    ]
}

allEfficiencyPlots = []
add_plot = allEfficiencyPlots.append
for variable, thresholds in six.iteritems(variables):
    for plot in plots[variable]:
        for threshold in thresholds:
            plotName = '{0}_threshold_{1}'.format(plot, threshold)
            add_plot(plotName)

from DQMOffline.L1Trigger.L1TEfficiencyHarvesting_cfi import l1tEfficiencyHarvesting
l1tTauEfficiency = l1tEfficiencyHarvesting.clone(
    plotCfgs=cms.untracked.VPSet(
        cms.untracked.PSet(
            numeratorDir=cms.untracked.string("L1T/L1TObjects/L1TTau/L1TriggerVsReco/efficiency_raw"),
            outputDir=cms.untracked.string("L1T/L1TObjects/L1TTau/L1TriggerVsReco"),
            numeratorSuffix=cms.untracked.string("_Num"),
            denominatorSuffix=cms.untracked.string("_Den"),
            plots=cms.untracked.vstring(allEfficiencyPlots),

        ),
    )
)

l1tTauEmuEfficiency = l1tEfficiencyHarvesting.clone(
    plotCfgs=cms.untracked.VPSet(
        cms.untracked.PSet(
            numeratorDir=cms.untracked.string(
                "L1TEMU/L1TObjects/L1TTau/L1TriggerVsReco/efficiency_raw"),
            outputDir=cms.untracked.string("L1TEMU/L1TObjects/L1TTau/L1TriggerVsReco"),
            numeratorSuffix=cms.untracked.string("_Num"),
            denominatorSuffix=cms.untracked.string("_Den"),
            plots=cms.untracked.vstring(allEfficiencyPlots),
        ),
    )
)
