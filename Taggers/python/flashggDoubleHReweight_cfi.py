import FWCore.ParameterSet.Config as cms

#default values first
weightsFile = ""

flashggDoubleHReweight = cms.EDProducer("FlashggDoubleHReweighter",
                                        GenParticleTag = cms.InputTag( "flashggPrunedGenParticles" ), # to compute MC-truth info
                                        doReweight = cms.int32(-1),  #it is only used to specify if reweighting has to be done : targetNode >  0 - yes 
                                        weightsFile = cms.untracked.FileInPath("%s"%weightsFile), 
                                        NCOEFFSA = cms.uint32(15), 
                                        A_13TeV_SM = cms.vdouble(2.09078, 10.1517, 0.282307, 0.101205, 1.33191, -8.51168, -1.37309, 2.82636, 1.45767, -4.91761, -0.675197, 1.86189, 0.321422, -0.836276, -0.568156),# coefficients of 15 operators for SM point
                                        benchmarks_map = cms.PSet( #values of kl,k5,c2,cg,c2g for 12 benchmarks and SM as 13th, box as 14th, wrong 2017 as 15th element in list (as in arxic 1507.02245 v4).
                                             kl = cms.vdouble(7.5,  1.0,  1.0, -3.5, 1.0, 2.4, 5.0, 15.0, 1.0, 10.0, 2.4, 15.0, 1., 0., 1.), 
                                             kt = cms.vdouble(1.0,  1.0,  1.0,  1.5, 1.0, 1.0, 1.0, 1.0,  1.0, 1.5 , 1.0, 1.0,  1., 1., 1. ), 
                                             c2 = cms.vdouble(-1.0, 0.5, -1.5, -3.0, 0.0, 0.0, 0.0, 0.0,  1.0, -1.0, 0.0, 1.0,  0., 0., 0.), 
                                             cg = cms.vdouble(0.0, -0.8,  0.0,  0.0, 0.8 ,0.2, 0.2,-1.0, -0.6, 0.0, 1.0, 0.0,   0., 0., 0.), 
                                             c2g = cms.vdouble(0.0, 0.6, -0.8,  0.0,-1.0,-0.2,-0.2, 1.0,  0.6, 0.0, -1.0, 0.0,  0., 0., 1.),
                                        )
                                        )

reweight_producer = "flashggDoubleHReweight"
reweight_names = ["benchmark0","benchmark1","benchmark2","benchmark3","benchmark4","benchmark5","benchmark6","benchmark7","benchmark8","benchmark9","benchmark10","benchmark11","benchmarkSM","benchmarkBox","benchmark2017fake","KL1","KL2","KL3","KL4","KL5","KL6","KL7","KL8","KL9","KL10","KL11","KL12","KL13","KL14","KL15","KL16","KL17","KL18","KL19","KL20","KL21","KL22","KL23","KL24","KL25","KL26","KL27","KL28","KL29","KL30","KL31","KL32","KL33","KL34","KL35","KL36","KL37","KL38","KL39","KL40","KL41","KL42","KL43","KL44","KL45","KL46","KL47","KL48","KL49","KL50","KL51","KL52","KL53","KL54","KL55","KL56","KL57","KL58","KL59","KL60","KL61","KL62","KL63","KL64","KL65","KL66","KL67","KL68","KL69","KL70","KL71","KL72","KL73","KL74","KL75","KL76","KL77","KL78","KL79","KL80"]
