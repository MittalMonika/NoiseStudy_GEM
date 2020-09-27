#/gemdata/GE11-M-12L2-L/scurve/2020.09.11.12.23/SCurveData/SCurveFitData.root
# >>> os.stat('somefile.txt').st_size
import sys 
import os 


import ROOT
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex



debuging_ = True

print len(sys.argv)
if ((len(sys.argv) < 3) | (len(sys.argv) > 3)): 
    print "insufficient input provided, please provide name of scandate and outputfilename"
    exit() 


timestampfile=""
outputfilename=""
if len(sys.argv) == 3:
    timestampfile=sys.argv[1]
    outputfilename=sys.argv[2]


#confdirname = "gemdata_"+timestampfile.split(".")[0]
#templatePath=confdirname+"/{}/scurve/{}/SCurveData/"
rootfilename="SCurveFitData.root"
chamberfile="chambersName.txt"

def TextFileToList(textfile="NONE"):
    return [iline.rstrip() for iline in open (textfile)]

def getChamber(filename):
    #print ("filename, ", filename)
    return filename.split("/")[-5]

cham_name = TextFileToList(chamberfile)
#    timestamps = TextFileToList(timestampfile)

alltimestamps=timestampfile.split(" ")


rootfileListForPlot=[]


#rootFileListTextFileList=[]
for itimestamp in alltimestamps:
    confdirname = "gemdata_"+itimestamp
    templatePath=confdirname+"/{}/scurve/{}/SCurveData/"

    #timestamps = TextFileToList(itimestamp)
    allrootfiles_name = "allrootfiles"+itimestamp
    #rootFileListTextFileList.append(allrootfiles_name)
    rootfileListForPlot.append("clean_"+allrootfiles_name)
    f_allrootfiles = open(allrootfiles_name,"w")
    
    
    for ichamb in cham_name:
        #for itime in timestamps:
        gemAreadir = templatePath.format(ichamb, itimestamp)
    
        if os.path.exists(gemAreadir):
            gemAreafile = gemAreadir+rootfilename
            if os.stat(gemAreafile).st_size > 1000 :
                f_allrootfiles.write(gemAreafile+"\n")
    
    f_allrootfiles.close()
    
                    
    localFileList = TextFileToList(allrootfiles_name)
    
    
    all_missing = [] 
    all_duplicate = []
    for ichamber in cham_name:
        icCounter=0
        
        chamber_duplicate=[]
        for ilocal in localFileList: 
            localChamb = getChamber(ilocal)
            if ichamber == localChamb: 
                chamber_duplicate.append(ilocal)
                icCounter+=1
        if icCounter >1: 
            #print ("duplicated file found: ", chamber_duplicate)
            all_duplicate.append(chamber_duplicate)
        if icCounter == 0: 
            #print ("missing chamber found: ", ichamber)
            all_missing.append(ichamber)
                
    
    print ("missing ------")
    print all_missing
    
    print ("duplicate ------")
    print all_duplicate
    
    
    if debuging_:
        if len(all_missing)>0:
            print ("We have found {} missing chamber rootfiles, do you want to proceed without them? ".format(len(all_missing) ))
            print ("Please enter  (y/Y) to proceed and (n/N) to stop here and debug :")
            value_ = raw_input()
            print ("you have entered "+value_)
            
            #value_ = str(value_)
            if (value_ == "y") | (value_ == "Y"):
                print ("lets have some fun with these histo, the missing file is replaced by a demo empty histogram to avoid crashes,  ")
                
                print ("all_missing: ",all_missing)
                
                template_empty_file = "summary.root"
                
#                fline=open(itimestamp).readline().rstrip()
                f_addmissing = open(allrootfiles_name,'a')
                for imissing in all_missing:
                    missing_dir=("missing_"+ templatePath.format(imissing, itimestamp))
                    os.system("mkdir -p "+missing_dir)
                    missingfilename_ = missing_dir+rootfilename
                    os.system("cp "+template_empty_file +" "+missingfilename_)
                    print ("cp "+template_empty_file +" "+missingfilename_)
                    f_addmissing.write(missingfilename_+"\n")

                f_addmissing.close()
                
            if (value_ == "n") | (value_ == "N"):
                print ("program execution stopped bye!!")
                exit()
            if not ((value_ == 'y') | (value_ == 'n') |(value_ == 'N') |(value_ == 'Y')) :
                print ("irrelevant input provided, code execution stopping here")
                exit()
    
    
        if len(all_duplicate)>0:
            print ("We have found duplicate chamber rootfiles, do you want to proceed to choose which one to use or skip running and remove duplicate offline. {}".format(len(all_duplicate) ))
            print ("Please enter a (c/C) to choose one  and (s/S) to skip running :")
            value_ = raw_input()
            print ("you have entered "+value_)
            if (value_ == "c") | (value_ == "C"):
                print ("choose the file: ")
                for idup in all_duplicate:
                    print "-----------"
                    for idupfile in idup:
                        os.system("ls -lhtr "+idupfile)
                    
                    value_choose = raw_input()
                    print ("you have chosen ",value_choose)
                    chosen_ = [value_choose]
                    all_dup_files_tmp_ = idup
                    to_remove_ = set(all_dup_files_tmp_) - set(chosen_)
                    
                    fout_ = open("clean_"+allrootfiles_name,"w")
                    
                    cleaned_files = set(localFileList)  - set(to_remove_)
                    
                    for ic_ in cleaned_files:
                        fout_.write(ic_+"\n")
                    fout_.close()
                                

            
            if (value_ == "s") | (value_ == "S"):
                print ("program execution stopped bye!!")
                exit()
            if not ((value_ == 's') | (value_ == 'S') |(value_ == 'c') |(value_ == 'C')) :
                print ("irrelevant input provided, code execution stopping here")
                exit()


        if len(all_duplicate)==0:
            os.system("cp "+allrootfiles_name+" clean_"+allrootfiles_name)



## plotting starts here 
all_files=[]
for ichamb in cham_name:
    files=[]
    for ifile in rootfileListForPlot:
        for irootfile in open(ifile,"r"):
            if ichamb in irootfile:
                files.append(irootfile.rstrip())
    all_files.append(files)

gStyle.SetOptTitle(0)


colors=[2,4,1,5,6,7,42,8,3]
Fsytle=[3004,3012,3007,3005,3305,3490,3456,3690]


c = TCanvas("c1", "c1",0,0,500,500)
c1_2 = TPad("c1_2","newpad",0.04,0.02,1,0.994)
c1_2.Draw()
c.cd()
c1_2.cd()

#conf_name_byhand= ['HVoff_MFoff_HCALoff_CSCoff_20200914', 'HVoff_MFon_HCALoff_CSCoff_20200911']
for ichm in range(len(all_files)):
    if ichm == 39 | ichm == 40:
        print ("monika: ",ichm, all_files[ichm])
    ## Legend                                                                                                                                                            
    leg = TLegend(0.09, 0.75, 0.89, 0.89)#,NULL,"brNDC");                                                                                                                             #leg.SetNColumns()
    leg.SetBorderSize(0)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(22)
    leg.SetTextSize(0.03)
    histList=[]
    chamber_name =[]
    conf_name =[]
    for ifile_ in all_files[ichm]:
            chamber_name.append(ifile_.split("/")[-5])
            conf_name.append(ifile_.split("/")[-3])
            inputfile = TFile(ifile_)
            if inputfile.IsZombie():
                continue
            histo = inputfile.Get("Summary/ScurveSigma_All")
            histo.SetDirectory(0)
            histo.AddDirectory(0)
            histList.append(histo)
    print ("histList: ",histList)
    for ih in range(len(histList)):
        if ih == 0:
            histList[ih].Draw("candle1")
        else:
            histList[ih].Draw("candle1 same")
        histList[ih].SetFillColor(colors[ih])
        histList[ih].SetLineColor(colors[ih])
        histList[ih].SetFillStyle(Fsytle[ih])
 
        leg.AddEntry(histList[ih],conf_name[ih],"F")
        histList[ih].GetYaxis().SetTitle("Noise(fC)")
        histList[ih].GetYaxis().SetTitleSize(0.052)
        histList[ih].GetYaxis().SetTitleOffset(0.88)
        histList[ih].GetYaxis().SetTitleFont(22)
        histList[ih].GetYaxis().SetLabelFont(22)
        histList[ih].GetYaxis().SetLabelSize(.052)
    #    histList[ih].GetXaxis().SetRangeUser(xRange[0],xRange[1])
        histList[ih].GetXaxis().SetLabelSize(0.0000);
        histList[ih].GetXaxis().SetTitle("VFATS")
        histList[ih].GetXaxis().SetLabelSize(0.052)
        histList[ih].GetXaxis().SetTitleSize(0.052)
        histList[ih].GetXaxis().SetTitleOffset(0.98)
        histList[ih].GetXaxis().SetTitleFont(22)
        histList[ih].GetXaxis().SetTickLength(0.07)
        histList[ih].GetXaxis().SetLabelFont(22)
        histList[ih].GetYaxis().SetLabelFont(22)
        histList[ih].GetXaxis().SetNdivisions(508)
    
    
    
    pt = TPaveText(0.0877181,0.9,0.9580537,0.96,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(22)
    pt.SetTextSize(0.046)
    pt.SetTextColor(38)
    text = pt.AddText(0.05,0.35,chamber_name[0])
    pt.Draw()
    leg.Draw()
    dirname = 'GEMPlots/'+outputfilename
    os.system("mkdir -p " + dirname)
#    dirname = 'GEMPlots/Comparison_20200921'
#    dirname = 'GEMPlots/Comparison_HVoff_MFon_HCALoff_CSCoff'
    c.SaveAs(dirname +'/'+chamber_name[0]+'.png')
    c.SaveAs(dirname +'/'+chamber_name[0]+'.pdf')


