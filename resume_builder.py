from fpdf import FPDF
from math import *
from array import *


class PDF(FPDF):
    def resumeName(self):
        # Arial bold-underlined 15
        self.set_font("Arial", "BU", 18)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_text_color(0, 0, 0)
        # Title
        self.cell(w, 20, title, 0, 1, "C")
        # Line break
        self.ln(1)

    def detailHeader(self, current_location, emailId, phoneNo, linkedIn):
        self.location = current_location
        self.email = emailId
        self.phone = phoneNo
        self.linkedInLink = linkedIn
        strDetailHeader = (
            self.location
            + " | "
            + self.email
            + " | "
            + self.phone
            + " | "
            + self.linkedInLink
        )
        # Arial 9
        self.set_font("Arial", "", 9)
        # Calculate width of title and position
        w = self.get_string_width(strDetailHeader) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_text_color(0, 0, 0)
        # Title
        self.write(9, self.location + " | ")
        # Then put a blue underlined link
        pdf.set_text_color(0, 0, 255)
        pdf.set_font("Arial", "U", 9)
        # pdf.write(9, self.email, self.email)
        pdf.write(9, self.email, f"mailto:{self.email}")
        # Arial 9
        self.set_font("Arial", "", 9)
        # Colors of frame, background and text
        self.set_text_color(0, 0, 0)
        self.write(9, " | " + self.phone + " | ")
        # Then put a blue underlined link
        pdf.set_text_color(0, 0, 255)
        pdf.set_font("Arial", "U", 9)
        pdf.write(9, self.linkedInLink, "https://www." + self.linkedInLink + "/")
        pdf.set_text_color(0, 0, 255)
        pdf.set_font("Arial", "", 9)
        # Line break
        self.ln(10)

    def appreciationComment(
        self, strAppreciation, strPresenter, strDesignation, strCompany
    ):
        self.appreciation = strAppreciation
        self.presenter = strPresenter
        self.designation = strDesignation
        self.company = strCompany
        self.set_text_color(0, 0, 0)
        self.set_font("Arial", "I", 10)
        self.multi_cell(0, 9, self.appreciation)
        # Line break
        self.ln(1)
        self.set_font("Arial", "", 10)
        self.cell(
            0,
            9,
            "~ " + self.presenter + ", " + self.designation + ", " + self.company,
            0,
            1,
            "R",
        )
        # Line break
        self.ln(10)

    def resumeHeadings(self, label):
        self.headingLabel = label
        # Arial 12
        self.set_font("Arial", "B", 11)
        # Background color
        self.set_text_color(0, 0, 139)
        # Title
        self.cell(0, 6, self.headingLabel, 0, 1, "L")
        self.set_draw_color(0, 0, 139)
        self.line(self.get_x(), self.get_y(), self.get_x() + 170, self.get_y())
        # Line break
        self.ln(10)

    def printSkillDetail(self, category, skill):
        self.skillCategory = category
        self.skillName = skill
        # Arial 12
        self.set_font("Arial", "B", 10)
        self.set_text_color(0, 0, 0)
        # Title
        self.write(2, self.skillCategory + ": ")
        self.set_font("Arial", "", 10)
        self.write(2, self.skillName)
        # Line break
        self.ln(10)

    def companyExperience(
        self, expCompany, expCity, expCountry, expDesignation, fDate, tDate
    ):
        self.companyExp = expCompany
        self.countryExp = expCountry
        self.cityExp = expCity
        self.designationExp = expDesignation
        self.fromDate = fDate
        self.toDate = tDate
        self.set_font("Arial", "B", 10)
        self.set_text_color(0, 0, 139)
        strwidth = 170 - self.get_string_width(
            self.companyExp + self.cityExp + "," + self.countryExp
        )
        strspace = ""
        for i in range(floor(strwidth)):
            strspace = strspace + " "
        self.write(2, self.companyExp + strspace)
        self.write(2, self.cityExp + "," + self.countryExp)
        # line break
        self.ln(7)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        strwidth = 170 - self.get_string_width(
            self.designationExp + self.fromDate + " - " + self.toDate
        )
        strspace = ""
        for i in range(floor(strwidth)):
            strspace = strspace + " "
        self.write(2, self.designationExp + strspace)
        self.write(2, self.fromDate + " - " + self.toDate)
        # line break
        self.ln(10)

    def educationDetails(
        self, strDegree, strCity, strCountry, strCollege, strUniversity, fDate, tDate
    ):
        self.degree = strDegree
        self.city = strCity
        self.country = strCountry
        self.college = strCollege
        self.university = strUniversity
        self.fromDate = fDate
        self.toDate = tDate
        self.set_font("Arial", "B", 10)
        self.set_text_color(0, 0, 139)
        strwidth = 170 - self.get_string_width(
            self.degree + self.city + ", " + self.country
        )
        strspace = ""
        for i in range(floor(strwidth)):
            strspace = strspace + " "
        self.write(2, self.degree + strspace)
        self.write(2, self.city + "," + self.country)
        # line break
        self.ln(7)
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        strwidth = 170 - self.get_string_width(
            self.college + ", " + self.university + self.fromDate + " - " + self.toDate
        )
        strspace = ""
        for i in range(floor(strwidth) - 2):
            strspace = strspace + " "
        self.write(2, self.college + ", " + self.university + strspace)
        self.write(2, self.fromDate + " - " + self.toDate)
        # line break
        self.ln(13)

    def displayInternship(self, arrInternship):
        for i in arrInternship:
            self.set_text_color(0, 0, 0)
            new_xcord = self.get_x()
            self.cell(0, 5, chr(127), 0, 0, "L")
            self.set_x(new_xcord + 5)
            self.set_font("Arial", "", 10)
            self.write(5, i)
            # line break
            self.ln(10)

    def displayAchievements(self, arrAchievement):
        for i in arrAchievement:
            self.set_text_color(0, 0, 0)
            new_xcord = self.get_x()
            self.cell(0, 5, chr(127), 0, 0, "L")
            self.set_x(new_xcord + 5)
            self.set_font("Arial", "", 10)
            self.write(5, i)
            # line break
            self.ln(10)

    def displayExtraCurricular(self, arrExtraCurricular):
        for i in arrExtraCurricular:
            self.set_text_color(0, 0, 0)
            new_xcord = self.get_x()
            self.cell(0, 5, chr(127), 0, 0, "L")
            self.set_x(new_xcord + 5)
            self.set_font("Arial", "", 10)
            self.write(5, i)
            # line break
            self.ln(10)


pdf = PDF()
# add margins first
pdf.l_margin = pdf.l_margin * 2.0
pdf.r_margin = pdf.r_margin * 2.0
pdf.t_margin = pdf.t_margin * 2.0
pdf.b_margin = pdf.b_margin * 2.0
pdf.line_width = pdf.line_width * 2.0

# take inputs from user
title = input("Enter your Full Name:")
location = input("Enter your current location:")
emailId = input("Enter your email Id:")
phoneNo = input("Enter your mobile number:")
linkedIn = input("Enter your Linked-In ID's link:")
strAppreciation = input(
    "Enter appreciation you received from your earlier project if any:"
)
if strAppreciation != "":
    strPresenter = input("Enter the Appreciation Presenter's name:")
    strDesignation = input("Enter presenter's Designation:")
    strPresenterCompany = input("Enter your company:")
pdf.add_page()
pdf.resumeName()
pdf.detailHeader(location, emailId, phoneNo, linkedIn)

if strAppreciation != "":
    pdf.appreciationComment(
        strAppreciation, strPresenter, strDesignation, strPresenterCompany
    )

# Collect Skill Details
pdf.resumeHeadings("SKILLS")
intNo_of_skills = 0
while intNo_of_skills == 0:
    intNo_of_skills = int(
        input(
            "Enter total number of skill Categories you wish to mention in your resume:"
        )
    )
    if intNo_of_skills == 0:
        print("Adding Skills to your Resume is mandatory. Please add atleast 1 skill.")
for i in range(0, intNo_of_skills):
    strCategory = input("Enter the category for the skill:")
    strSkillList = input("Enter your list of skills(seperated by comma ','):")
    pdf.printSkillDetail(strCategory, strSkillList)

# Collect Experience details
pdf.resumeHeadings("EXPERIENCE")
intNo_of_CompanyExp = int(input("Enter number of Companies you've your experience in:"))
for i in range(0, intNo_of_CompanyExp):
    strCompany = input("Enter Company name (in CAPITAL):")
    strCity = input("Enter City name (in CAPITAL):")
    strCountry = input("Enter Country name (in CAPITAL):")
    strDesignation = input("Enter Designation in this company:")
    strFromDate = input(
        "Enter the Date from which you  started working for this company (Format: MM/YYYY):"
    )
    strToDate = input(
        "Enter the Date till which you worked for this company (Format: MM/YYYY or mention 'Ongoing' if you're currently working here):"
    )
    pdf.companyExperience(
        strCompany, strCity, strCountry, strDesignation, strFromDate, strToDate
    )

# Collect Education Details
pdf.resumeHeadings("EDUCATION")
print("Enter your Latest two Education details:")
for i in range(2):
    strDegreeName = input("Enter your Degree name (in CAPITAL):")
    strCity_of_Degree = input(
        "Enter the city in which you completed your Degree (in CAPITAL):"
    )
    strCountry_of_Degree = input(
        "Enter the country in which you completed your Degree (in CAPITAL):"
    )
    strCollege = input("Enter College name from which you have completed your Degree:")
    strUniversity = input("Enter the University name for your Degree:")
    strFromDate_of_Degree = input(
        "Enter the Date from which you started your mentioned Education (Format: MM/YYYY):"
    )
    strToDate_of_Degree = input(
        "Enter the Date till you completed your Degree (Format: MM/YYYY or mention 'Ongoing' if you're currently perceiving education here):"
    )
    pdf.educationDetails(
        strDegreeName,
        strCity_of_Degree,
        strCountry_of_Degree,
        strCollege,
        strUniversity,
        strFromDate_of_Degree,
        strToDate_of_Degree,
    )

# Collect Internships details
intNo_of_internships = int(
    input("Enter number of internships you wish to mention in resume:")
)
internshipList = []
if intNo_of_internships != 0:
    pdf.resumeHeadings("INTERNSHIP")
    for i in range(0, intNo_of_internships):
        strInternshipDesc = input("Enter your internship Description in one line:")
        internshipList.append(strInternshipDesc)
    pdf.displayInternship(internshipList)

# Collect Achievement details
intNo_of_Achievements = int(
    input("Enter number of achievements you wish to mention in resume:")
)
achievementList = []
if intNo_of_Achievements != 0:
    pdf.resumeHeadings("ACHIEVEMENTS")
    for i in range(0, intNo_of_Achievements):
        strAchievementDesc = input("Enter your achievement Description in one line:")
        achievementList.append(strAchievementDesc)
    pdf.displayAchievements(achievementList)

# Collect Extra curricular activities details
intNo_of_ExtraCurricularAct = int(
    input("Enter number of Extra Curricular Activities you wish to mention in resume:")
)
extraCurricularList = []
if intNo_of_ExtraCurricularAct != 0:
    pdf.resumeHeadings("EXTRA - CURRICULAR ACTIVITIES")
    for i in range(0, intNo_of_ExtraCurricularAct):
        strExtraCurricularActDesc = input(
            "Enter your achievement Description in one line:"
        )
        extraCurricularList.append(strExtraCurricularActDesc)
    pdf.displayAchievements(extraCurricularList)

# line break
pdf.ln(10)
pdf.set_font("Arial", "", 11)
pdf.set_draw_color(0, 0, 0)
pdf.line(pdf.get_x() + 65, pdf.get_y(), pdf.get_x() + 105, pdf.get_y())

pdf.output("resume.pdf", "F")
