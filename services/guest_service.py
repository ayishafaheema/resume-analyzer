import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from utils.file_extractor import extract_text
import readfile




class GuestResumeAnalyzer:
    def __init__(self,job_description="",resume="",job_file=None,resume_file=None):
        self.job_description=job_description or ""
        self.resume=resume or ""
        self.job_file=job_file
        self.resume_file=resume_file
        
    def analyze(self):
        self.load_files()
        
        print("JD text:", self.job_description)
        print("Resume text:", self.resume)


        if not self.job_description.strip() or not self.resume.strip():
            return {
                "matches": [],
                "missing": [],
                "matched_count": 0,
                "missing_count": 0,
                "chart_path": None
            }

        
        matches,missing=self.analyze_text()
        chart_path = self.create_pie_chart(len(matches), len(missing))
        return {
                    "matches": matches,
                    "missing": missing,
                    "matched_count": len(matches),
                    "missing_count": len(missing),
                    "chart_path": chart_path
                }
        
        
        
    def load_files(self):
        if self.job_file and self.job_file.filename:
            self.job_description=extract_text(
                self.job_file,self.job_file.filename
            )
        if self.resume_file and self.resume_file.filename:
            self.resume=extract_text(
                self.resume_file,self.resume_file.filename
            )    
            
    def analyze_text(self):
        return readfile.analyze_resume(
            self.job_description,
            self.resume
        )
        
    def create_pie_chart(self,matched,missing):
        labels=["Matched","Missing"]
        if matched == 0 and missing == 0:
           matched = 1
        sizes=[matched,missing]

        plt.figure(figsize=(4.5, 4))
        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title("Resume Keyword Match")
        chart_path = os.path.join("static", "guest_chart.png")
        plt.savefig(chart_path)
        plt.close()
        return chart_path