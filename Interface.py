## This File is the Program Interface
# Bibliotecas importadas
from cdi import *
from tkinter import *

# @class Application

class Application():
    
    def __init__(self, master = None):
        # creating window
        self.Frame1 = Tk()
        #self.Frame1.configure(relief='solid', border='1.2px', background='#cac3ba')
        # Windows Configs
        self.Frame1.title('CDI App')
        self.Frame1.geometry('520x640+100+100')
        #self.Frame1.resizable(True, True)
        self.Frame1.minsize(width=485, height=540)
        self.Frame1.maxsize(width=600, height=720)   # at this moment

        # calling the functions
        self.framesWindow()
        self.titleL()
        self.principal()
        self.footer()
        mainloop()


    # fonts and colors variables
    varlb_font = 'verdana 12 bold'  # AppleMyungjo
    varlb_bg = 'lightgray'
    varlb_font2 = 'verdana 11 bold' # Final Left and Right Fonts


    # Frames Window
    def framesWindow(self):
        # Creating the frames
        self.frameWin = Frame(self.Frame1, relief='solid',border='1px', background='#cac3ba')
        self.frameWin.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.framePrincipal = Frame(self.frameWin, relief='raised', border='3px', background='#faebd7')
        self.framePrincipal.place(relx=0.03, rely=0.14, relwidth=0.92, relheight=0.75)
    

    def titleL(self):
        self.titleT = Label(self.frameWin, text='CDBs, LCIs e LCAs indexadas por\nCertificados de Depósitos Interbancários')
        self.titleT.place(relx=0.05, rely=0.02, relwidth=0.86, relheight=0.1)
        self.titleT.configure(relief='ridge',bd='5px', font='Arial 14 bold', justify='left', background='#ff6347')   # highlightbackground='lightblue', highlightthickness=3 --> Optional
    
    def principal(self):
        
        # Creating Capital label and entry 
        self.lbCapital = Label(self.framePrincipal, text='Capital:                      $', bg='#faebd7', font=('verdana', 12))
        self.lbCapital.place(relx=0.02, rely=0.02)
        self.capitalEntry = Entry(self.framePrincipal)   # textvariable=self.varCapital
        self.capitalEntry.place(relx=0.5, rely=0.023, relwidth=0.3, relheight=0.05)

        # Creating TaxaSelic label and entry
        self.lbTaxSelic = Label(self.framePrincipal, text='Taxa Selic: ', bg='#faebd7', font=('verdana', 12))
        self.lbTaxSelic.place(relx=0.02, rely=0.12)
        self.taxSelicEntry = Entry(self.framePrincipal)
        self.taxSelicEntry.place(relx=0.5, rely=0.123, relwidth=0.2, relheight=0.05)

        # Creating TaxaCDI label and entry
        self.lbTaxCDI = Label(self.framePrincipal, text='Taxa CDI: ', bg='#faebd7', font=('verdana', 12))
        self.lbTaxCDI.place(relx=0.02, rely=0.22)
        self.taxCDIEntry = Entry(self.framePrincipal)
        self.taxCDIEntry.place(relx=0.5, rely=0.223, relwidth=0.2, relheight=0.05)

        # Creating Rentabilidade label and entry
        self.lbRentability = Label(self.framePrincipal, text='Rentabilidade: ', bg='#faebd7', font=('verdana', 12))
        self.lbRentability.place(relx=0.02, rely=0.32)
        self.rentabilityEntry = Entry(self.framePrincipal)
        self.rentabilityEntry.place(relx=0.5, rely=0.323, relwidth=0.2, relheight=0.05)

        # Creating Meses label and entry
        self.lbMonths = Label(self.framePrincipal, text='Meses: ', bg='#faebd7', font=('verdana', 12))
        self.lbMonths.place(relx=0.02, rely=0.42)
        self.monthsEntry = Entry(self.framePrincipal)
        self.monthsEntry.place(relx=0.5, rely=0.423, relwidth=0.2, relheight=0.05)

        # Creating Alíquota label and radioButtons
        self.lbAliquote = Label(self.framePrincipal, text='Alíquota IR: ', bg='#faebd7', font=('verdana', 12))
        self.lbAliquote.place(relx=0.02, rely=0.52)
        
        # valueOpt is a variable that store the value of an option
        self.valueOpt = IntVar(self.framePrincipal, 22.5)
        self.valueOpt.set(22.5)   # set opt5 with value equal 22.5

        self.Opt1 = Radiobutton(self.framePrincipal, text='0.0 (LCA ou LCI)', variable=self.valueOpt, value=0, bg='#faebd7', font=('verdana', 12))
        self.Opt1.place(anchor=W, relx=0.08, rely=0.62)

        self.Opt2 = Radiobutton(self.framePrincipal, text='15.0 (acima de 721 dias)', variable=self.valueOpt, value=15.0, bg='#faebd7', font=('verdana', 12))
        self.Opt2.place(anchor=W, relx=0.08, rely=0.7)
        
        self.Opt3 = Radiobutton(self.framePrincipal, text='17.5 (de 361 até 720 dias)', variable=self.valueOpt,value=17.5, bg='#faebd7', font=('verdana', 12))
        self.Opt3.place(anchor=W, relx=0.08, rely=0.78)

        self.Opt4 = Radiobutton(self.framePrincipal, text='20.0 (de 181 até 360 dias)', variable=self.valueOpt, value=20.0, bg='#faebd7', font=('verdana', 12))
        self.Opt4.place(anchor=W, relx=0.08, rely=0.86)

        self.Opt5 = Radiobutton(self.framePrincipal, text='22.5 (até 180 dias)', variable=self.valueOpt, value=22.5, bg='#faebd7', font=('verdana', 12))
        self.Opt5.place(anchor=W, relx=0.08, rely=0.94)

    def NewWindowResult(self):

        self.FrameSecondary = Tk()
        self.FrameSecondary.title('CDI App Result')
        self.FrameSecondary.geometry('680x650+660+100')
        self.FrameSecondary.minsize(width=700, height=640)

        self.framesWindowResult()
        self.CDIResult()
        mainloop()

    def framesWindowResult(self):

        # Frame green top
        self.InitialFrameResult = Frame(self.FrameSecondary, bg='lightgray', highlightthickness=5, highlightbackground='green')
        self.InitialFrameResult.place(relx=0.02, rely=0.02, relwidth=0.96, relheight= 0.46)
        
        # Frame bottom that frame joins two other frames
        self.FinalFrameResult = Frame(self.FrameSecondary, bd=5)
        self.FinalFrameResult.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        
        # Frame blue left bottom
        self.FinalLeftFrameResult = Frame(self.FinalFrameResult, bg='lightgray', highlightthickness=5, highlightbackground='blue')
        self.FinalLeftFrameResult.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        
        # Frame red right bottom
        self.FinalRightFrameResult = Frame(self.FinalFrameResult, bg='lightgray', highlightthickness=5, highlightbackground='red')
        self.FinalRightFrameResult.place(relx=0.52, rely=0, relwidth=0.48, relheight=1)

    def CDIResult(self):

        def Decimal(x):
            return x / 100

        # creating variables and storing the values
        # self.txCDIValuePF is self.txCDIValue floating point
        self.capitalValue = float(self.capitalEntry.get())
        self.txSelicValue = float(self.taxSelicEntry.get())
        self.txCDIValue = float(self.taxCDIEntry.get()); self.txCDIValuePF = Decimal(self.txCDIValue) 
        self.txCDIValueM = BFunc.year2month(self, self.txCDIValuePF); self.txCDIValueD = BFunc.year2day(self, self.txCDIValuePF)

        self.txPoupValueA = float(BFunc.checkAmountSavings(self, self.txSelicValue)); self.txPoupValueM = BFunc.year2month(self, Decimal(self.txPoupValueA))
        
        self.RentabilityValue = float(self.rentabilityEntry.get()); self.RentabilityValueA = (self.RentabilityValue * Decimal(self.txCDIValue))
        
        self.MonthValue = int(self.monthsEntry.get())

        # IR value condition according to month
        if self.MonthValue <= 6:
            self.IRValue = 22.5
        elif self.MonthValue >= 7 and self.MonthValue <= 12:
            self.IRValue = 20.0
        elif self.MonthValue >= 13 and self.MonthValue <= 24:
            self.IRValue = 17.5
        else:
            self.IRValue = 15
        # set Radio Opt value 
        self.valueOpt.set(self.IRValue)

        # Values return by CDB Function
        self.RentImp, self.RentImpA, self.applicationAmount, self.savingsAmount, self.amountAppl_Poup, self.TaxWithholding, self.profitabilityMonths, self.percAppl_Poup, self.AppliEqualPoup, self.t2xPoupA, self.t2xAppliA = BFunc.CDB(self, self.capitalValue, self.txCDIValuePF, self.txPoupValueA, self.RentabilityValue, self.IRValue, self.MonthValue)


        """ Arrange the ELEMENTS INFORMATIONS on the GREEN SCREEN FRAME """
        # Capital Value
        self.lb_Capital = Label(self.InitialFrameResult, text=f'Capital: ${self.capitalValue:.2f}', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_Capital.place(relx=0.02, rely=0.02)

        # Taxa Selic Value
        self.lb_txSelic = Label(self.InitialFrameResult, text=f'Taxa Selic: {self.txSelicValue:.2f}% ao ano', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_txSelic.place(relx=0.02, rely=0.15)

        # CDI Value Annual, Monthly and Daily
        self.lb_txCDI = Label(self.InitialFrameResult, text=f'CDI: {self.txCDIValue:.2f}% ao ano = {self.txCDIValueM:.4f}% ao mês = {self.txCDIValueD:.6f}% ao dia', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_txCDI.place(relx=0.02, rely= 0.28)

        # Taxa Poup Value Annual and Monthly
        self.lb_txPoup = Label(self.InitialFrameResult, text=f'Taxa Poupança: {self.txPoupValueA}% ao ano = {self.txPoupValueM:.4f}% ao mês', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_txPoup.place(relx=0.02, rely=0.41)

        # IR
        self.lb_IR = Label(self.InitialFrameResult, text=f'IR = {self.IRValue}%', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_IR.place(relx=0.02, rely=0.54)

        # RENTABILITY VALUE 
        self.lb_rentability = Label(self.InitialFrameResult, text=f'Rentabilidade: {self.RentabilityValue}% CDI = {self.RentabilityValueA:.2f}% ao ano', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_rentability.place(relx=0.02, rely=0.67)

        # RENTABILITY VALUE WITH TAX
        self.lb_rentabilityImp = Label(self.InitialFrameResult, text=f'Com Impostos: {self.RentImp:.2f}% CDI = {self.RentImpA:.2f}% ao ano', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_rentabilityImp.place(relx=0.02, rely=0.75)

        # MONTH Value
        self.lb_Month = Label(self.InitialFrameResult, text=f'Meses: {self.MonthValue}', font=self.varlb_font, bg=self.varlb_bg)
        self.lb_Month.place(relx=0.02, rely=0.88)

        """ Arrange the ELEMENTS INFORMATIONS on the BLUE SCREEN FRAME """
        # AMOUNTAPL Value
        self.lb_ApplAmount = Label(self.FinalLeftFrameResult, text=f'Montante Aplicação = ${self.applicationAmount:.2f}', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_ApplAmount.place(relx=0.02, rely=0.1)

        # SAVINGSAMOUNT Value
        self.lb_SavingsAmount = Label(self.FinalLeftFrameResult, text=f'Montante Poupança = ${self.savingsAmount:.2f}', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_SavingsAmount.place(relx=0.02, rely=0.25)
        
        # APL - POUP Value
        self.lb_AmountApl_Poup = Label(self.FinalLeftFrameResult, text=f'Apl - Poup ({self.MonthValue} meses) = ${self.amountAppl_Poup:.2f}', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_AmountApl_Poup.place(relx=0.02, rely=0.4)

        # TAX RATE Value
        self.lb_TaxRate = Label(self.FinalLeftFrameResult, text=f'Imposto = ${self.TaxWithholding:.4f}', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_TaxRate.place(relx=0.02, rely=0.55)

        # PROFITABILITY IN MONTHS
        self.lb_ProfMonths = Label(self.FinalLeftFrameResult, text=f'Rendimento em {self.MonthValue} meses = {self.profitabilityMonths:.4}%', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_ProfMonths.place(relx=0.02, rely=0.7)

        """ Arrange the ELEMENTS INFORMATIONS on the RED SCREEN FRAME """
        # APL - POUP PERCENTAGE Value
        self.lb_AmountApl_PoupPerc = Label(self.FinalRightFrameResult, text=f'Apl - Poup ({self.MonthValue} meses) = {self.percAppl_Poup:.4f}%', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_AmountApl_PoupPerc.place(relx=0.02, rely=0.15)

        # APL = POUP PERCENTAGE Value
        self.lb_AppliEqualPoup = Label(self.FinalRightFrameResult, text=f'Apl = Poup = {self.AppliEqualPoup:.2f}% CDI', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_AppliEqualPoup.place(relx=0.02, rely=0.32)

        # TIME 2 x SAVINGS Value
        self.lb_t2xPoupA = Label(self.FinalRightFrameResult, text=f'Tempo 2 x Poupança = {self.t2xPoupA:.2f} anos', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_t2xPoupA.place(relx=0.02, rely=0.49)

        # TIME 2 x APPLICATION Value
        self.lb_t2xAppliA = Label(self.FinalRightFrameResult, text=f'Tempo 2 x Aplicação = {self.t2xAppliA:.2f} anos', font=self.varlb_font2, bg=self.varlb_bg)
        self.lb_t2xAppliA.place(relx=0.02, rely=0.66)

    # Button position
    def footer(self):
        self.button = Button(self.frameWin, text='Calcular', command=self.NewWindowResult)
        self.button.place(relx=0.45, rely=0.905)
        self.button.configure(relief='solid', bd='1px', bg='#faebd7',font='Arial 10', foreground='red', width=8, height=1)

        # HoverButton change color
        def on_enter(e):
            self.button['background'] = '#fadad7'
        def on_leave(e):
            self.button['background'] = '#faebd7'
        
        # change method
        self.button.bind('<Enter>', on_enter)
        self.button.bind('<Leave>', on_leave)

    
app = Application()