import sys 
import os 



#dirname=["HVoff_MFoff_HCALoff_CSCoff_20200921_1707","HVoff_MFon_HCALoff_CSCon_20200925"]

dirname=["HVoff_MFoff_HCALoff_CSCoff_20200921_1707",
"BenchPSOnChamb_L1onL2off_LVoff_HVoff_MFon_HCALoff_CSCoff_20200925",
"BenchPSOnChamb_SingleSC_LVoff_HVoff_MFon_HCALoff_CSCoff_20200925",
"BenchPSOnChamb_SingleSC_LVon_HVoff_MFon_HCALoff_CSCoff_20200925"]

#dirname = ["HVoff_MFoff_HCALoff_CSCoff_20200921_1707","SC25_HVoff_MFoff_HCALoff_CSCoff_20200923","SC25_SC24LVon_HVoff_MFoff_HCALoff_CSCoff_20200923","SC25_SC24LVon_SC24HVon_HVoff_MFon_HCALoff_CSCoff_20200923","SC25_SC24LVoff_SC24HVon_HVoff_MFon_HCALoff_CSCoff_20200923","SC25_SC25HVon_SC24LVon_SC24HVon_HVoff_MFon_HCALoff_CSCoff_20200923","SC25_HVon_MFon_HCALoff_CSCoff_20200923","SC25_SC25HVon_HVoff_MFon_HCALoff_CSCoff_20200923"]


#dirname = ["HVoff_MFoff_HCALoff_CSCoff_20200921_1707","SingleLayer_HVoff_MFoff_HCALoff_CSCoff_20200922","BenchPSOnChamb_L1dis_HVoff_MFoff_HCALoff_CSCoff_20200924","BenchPSOnChamb_L1dis_LVon_HVoff_MFoff_HCALoff_CSCoff_20200924","BenchPSOnChamb_L1con_LVon_HVoff_MFoff_HCALoff_CSCoff_20200924","BenchPSOnChamb_L1con_LVoff_HVoff_MFoff_HCALoff_CSCoff_2020924"]




#dirname=["HVoff_MFoff_HCALoff_CSCoff_20200921_1707",
#"SingleLayer_HVoff_MFoff_HCALoff_CSCoff_20200922",
#"BenchPSOnChamb_L1dis_LVoff_HVoff_MFon_HCALoff_CSCoff_20200924",
#"BenchPSOnChamb_L1on_LVoff_HVoff_MFon_HCALoff_CSCoff_20200924",
#"BenchPSOnChamb_L1on_LVon_HVoff_MFon_HCALoff_CSCoff_20200924",
#"BenchPSOnRack_L1dis_LVoff_HVoff_MFon_HCALoff_CSCoff_20200925",
#"BenchPSOnRack_L1on_LVoff_HVoff_MFon_HCALoff_CSCoff_20200925",
#"BenchPSOnRack_L1on_LVon_HVoff_MFon_HCALoff_CSCoff_20200925"]


#dirname=["HVoff_MFoff_HCALoff_CSCoff_20200921_1707",
#"BenchPSOnChamb_L1L2_LVoff_HVoff_MFon_HCALoff_CSCoff_20200925",
#"BenchPSOnChamb_L1L2_LVon_HVoff_MFon_HCALoff_CSCoff_20200925"]

for i in dirname:
    print i
    os.system("python Copycmsusr_symlinks.py " + i )



x = " ".join(dirname)
#os.system("python plotENC_symlinks.py "+ """'"""+x+"""'""" + " Comparison_Chamber25" )
#os.system("python plotENC_symlinks.py "+ """'"""+x+"""'""" + " Comparison_CSC_off_and_on" )
os.system("python plotENC_symlinks.py "+ """'"""+x+"""'""" + " Comparison_BenchPSOnChamb_22" )
