import FWCore.ParameterSet.Config as cms

quickTrackAssociatorByHits = cms.EDProducer("QuickTrackAssociatorByHitsProducer",
	AbsoluteNumberOfHits = cms.bool(False),
	Cut_RecoToSim = cms.double(0.75),
	SimToRecoDenominator = cms.string('reco'), # either "sim" or "reco"
	Quality_SimToReco = cms.double(0.5),
	Purity_SimToReco = cms.double(0.75),
	ThreeHitTracksAreSpecial = cms.bool(True),
        PixelHitWeight = cms.double(1.0),
        useClusterTPAssociation = cms.bool(True),
        cluster2TPSrc = cms.InputTag("tpClusterProducer")
)

from Configuration.Eras.Modifier_fastSim_cff import fastSim
fastSim.toModify(quickTrackAssociatorByHits,
    useClusterTPAssociation = False,
    associateStrip = cms.bool(False),
    associatePixel = cms.bool(False),
    pixelSimLinkSrc = cms.InputTag("simSiPixelDigis"),
    stripSimLinkSrc = cms.InputTag("simSiStripDigis"),
)

from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2
(fastSim & premix_stage2).toModify(quickTrackAssociatorByHits,
    pixelSimLinkSrc = "mixData:PixelDigiSimLink",
    stripSimLinkSrc = "mixData:StripDigiSimLink",
)
