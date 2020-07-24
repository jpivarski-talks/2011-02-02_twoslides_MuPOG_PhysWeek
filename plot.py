import ROOT
execfile("/home/pivarski/bin/root/tdrstyle.py")
c1 = ROOT.TCanvas()
c1.SetLogx(1)
c1.SetLogy(1)

h = ROOT.TH1F("h", "", 1, 3., 1000.)
f15 = ROOT.TF1("f15", "sqrt((7./sqrt(x))**2 + 0.2**2)", 3., 1000.)
f20 = ROOT.TF1("f20", "sqrt((9.9/sqrt(x))**2 + 0.2**2)", 3., 1000.)
fmb1 = ROOT.TF1("fmb1", "sqrt((4.7/sqrt(x))**2 + 0.2**2)", 3., 1000.)
fme11 = ROOT.TF1("fme11", "sqrt((2.7/sqrt(x))**2 + 0.2**2)", 3., 1000.)
fhnow = ROOT.TF1("fhnow", "1.", 3., 1000.)
fhult = ROOT.TF1("fhult", "0.2", 3., 1000.)
fbh = ROOT.TF1("fbh", "0.35", 3., 1000.)

for f in f15, fhult:
    f.SetLineStyle(2)

for f in fme11, fbh:
    f.SetLineColor(ROOT.kBlue)

for f in fmb1, fhnow, fhult:
    f.SetLineColor(ROOT.kRed)

for f in f15, f20:
    f.SetLineColor(ROOT.kBlack)

for f in f15, f20, fmb1, fme11, fhnow, fhult, fbh:
    f.SetLineWidth(2)

h.SetAxisRange(0.1, 10., "Y")
h.SetXTitle("collisions data [pb^{-1}]")
h.SetYTitle("r#phi chamber position resolution [mm]")
h.GetXaxis().CenterTitle()
h.GetYaxis().CenterTitle()

h.Draw()
f20.Draw("same")
f15.Draw("same")
fmb1.Draw("same")
fme11.Draw("same")
fhnow.Draw("same")
fhult.Draw("same")
fbh.Draw("same")
tline1 = ROOT.TLine(35., 0.1, 35., 10.); tline1.SetLineStyle(3); tline1.Draw()
tline2 = ROOT.TLine(210., 0.1, 210., 10.); tline2.SetLineStyle(3); tline2.Draw()

tlegend = ROOT.TLegend(0.65, 0.75, 0.9, 0.9)
tlegend.SetFillColor(ROOT.kWhite); tlegend.SetBorderSize(1)
tlegend.AddEntry(f20, "all chambers", "l")
tlegend.AddEntry(fhnow, "barrel", "l")
tlegend.AddEntry(fbh, "endcap", "l")
tlegend.Draw()

c1.SaveAs("projections.pdf")
