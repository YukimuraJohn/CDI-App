# Bibliotecas importadas
import math as math
import sys
import getopt

# @class BasicFunctions as BFunc


class BFunc:

    ## Juros compostos.
    # É a adição de juros ao capital principal de um empréstimo ou depósito,
    # ou em outras palavras, juros sobre juros.
    #
    # É o resultado do reinvestimento dos juros, ao invés de pagá-lo,
    # de tal forma que a taxa no próximo período é calculada
    # sobre o principal , mais os juros recebidos previamente.
    #
    # A função de acumulação mostra como uma unidade monetária
    # cresce após o período de tempo.
    #
    # @param r taxa de juros nominal.
    # @param t período de tempo total no qual os juros são aplicados
    # ( expressa nas mesmas unidades de tempo de r, usualmente anos ).
    # @param n frequência de composição ( pagamento dos juros ), por exemplo,
    # mensal , trimestral ou anual.
    # @return juros obtidos no período : (1 + r/n)^nt - 1

    def jc(self, r: float, t: int, n: int = 1) -> float:

        return (1 + r / float(n))**(n * t) - 1


    ## Converte uma taxa de juros anual para uma taxa diaria.
    # Em matemática financeira, consideramos 252 dias por ano.
    #
    # @param a taxa de juros anual.
    # @return taxa de juros diario dada a taxa anual,
    # na forma de um percentual.

    def year2day(self, a: float):

        return 100 * BFunc.jc(self, a, 1 / 252.0)

    ## Converte uma taxa de juros anual para uma taxa mensal.
    #
    # @param a taxa de juros anual.
    # @return taxa de juros mensal dada a taxa anual,
    # na forma de um percentual.

    def year2month(self, a: float) -> float:

        return 100 * (BFunc.jc(self, a, 1 / 12.0))

    # Calcula o logaritmo de 2 na base 1 + r.
    # Pode ser aproximado por 72/(100 ∗ r).
    #
    # É usada para calcular o tempo necessário
    # para dobrar o principal quando sujeito uma taxa de juros dada .
    #
    # @param r taxa de juros nominal .
    # @return tempo para dobrar o principal .

    def doublePrincipal(self, r: float) -> float:

        return math.log(2, 1 + r)

    # Check Amount Savings compare if selic is less than or equal to 8.5%,
    # txPoup will receive selic * 0.7, or if it's greater than 8.5 txPoup
    # receive 6.17
    # @param s taxa selic
    # @return annual savings and monthly savings

    def checkAmountSavings(self, s: float) -> float:
        self.selic = s

        if self.selic <= 8.5:
            self.txPoup = 0.7 * self.selic
        else:
            self.txPoup = 6.17

        return self.txPoup

    # Calcula o montante final, imposto, rendimento e rentabilidade equivalente.
    #
    # @param c capital
    # @param cdi taxa cdi anual
    # @param p taxa poupança anual = 0.70 * selic
    # @param t rentabilidade da aplicação em função do CDI
    # @param i alíquota do imposto de renda
    # @param m meses
    # @return
    # - montante da aplicação,
    # - montante poupança,
    # - imposto de renda retido,
    # - rendimento em m meses (%),
    # - rendimento em m meses,
    # - rendimento líquido em 1 mês,
    # - rentabilidade para igualar poupança (%) CDI
    def CDB(self, c: float, cdi: float, p: float, t: float, i: float, m: int = 1) -> float:
        self.cap = c
        self.cdiA = cdi
        self.txCDI = t
        self.txPoupA = p

        # Checking the month and changing the IR value
        if m <= 6:
            i = 22.5
        elif m >= 7 and m <= 12:
            i = 20.0
        elif m >= 13 and m <= 24:
            i = 17.5
        else:
            i = 15.0

        # Printing IR value before checking the month
        # print(f'IR = {i}%\n')

        """Profitability without tax """
        # Profitability (yearlycdi * tax cdi)/100
        txCDIA = (self.cdiA * self.txCDI)

        # Profitability txCDIA is converting to monthly amount
        txCDIM = BFunc.year2month(self, txCDIA/100)

        """Profitability with tax """
        txCDI_Imp = ((100 - i) * self.txCDI/100)
        txCDI_ImpA = (txCDI_Imp * self.cdiA)

        # txCDI_ImpA_Mes is the monthly percentage value for CDI tax ImpA
        txCDI_ImpA_Mes = BFunc.year2month(self, txCDI_ImpA/100)

        # Printing Profitability without tax and with tax
        # print(f'Rentabilidade = {self.txCDI}% CDI = {txCDIA:.2f}% ao ano')
        # print(
        #     f'Com Imposto = {txCDI_Imp:.2f}% CDI = {txCDI_ImpA:.2f}% ao ano\n')
        # print(f'Meses = {m}\n')

        
        """Part --> Apl - Poup (m months)$ Amount"""
        # Application Amount value
        applicationAmount = self.cap + ((txCDI_ImpA_Mes/100 * self.cap)*m)
        # txPoupM is being multiplied by m
        txPoupM = BFunc.year2month(self, self.txPoupA/100)
        savingsAmount = self.cap + (((txPoupM) * m / 100)*self.cap)
        # Apl - Poup (m months)$ Amount
        amountAppl_Poup = applicationAmount - savingsAmount
        # print(f'Montante Aplicação = ${applicationAmount:.2f}')
        # print(f'Montante Poupança = ${savingsAmount:.2f}')
        # print(f'Apl - Poup ({m} meses) = ${amountAppl_Poup:.2f}')

        TaxWithholding = (
            self.cap + (self.cap * ((txCDIM/100) * m))) - applicationAmount
        # print(f'Imposto = ${TaxWithholding:.4f}')

        """Profitability in months"""
        profitabilityMonths = ((applicationAmount - self.cap) * 100)/self.cap
        # print(f'Rendimento em {m} meses = {profitabilityMonths:.4f}%\n')


        """New Part --> Apl - Poup (m months)% Percentage"""
        percAppl_Poup = (amountAppl_Poup * 100)/self.cap
        # print(f'Apl - Poup ({m} meses) = {percAppl_Poup:.4f}%')

        # Apl = Poup
        AppliEqualPoup = self.txPoupA / (self.cdiA * (1 - i/100))
        # print(f'Apl = Poup = {AppliEqualPoup:.2f}% CDI')

        # Time 2 x Savings
        t2xPoupA = BFunc.doublePrincipal(self, self.txPoupA/100)
        #t2xPoupM = self.doublePrincipal(txPoupM/100)
        # print(
        #     f'Tempo 2 x Poupança = {t2xPoupA:.2f} anos = {t2xPoupM:.2f} meses')

        # Time 2 x Application
        t2xAppliA = BFunc.doublePrincipal(self, txCDI_ImpA/100)
        #t2xAppliM = self.doublePrincipal(txCDI_ImpA_Mes/100)
        # print(
        #     f'Tempo 2 x Aplicação = {t2xAppliA:.2f} anos = {t2xAppliM:.2f} meses')

        return txCDI_Imp, txCDI_ImpA, applicationAmount, savingsAmount, amountAppl_Poup, TaxWithholding, profitabilityMonths, percAppl_Poup, AppliEqualPoup, t2xPoupA, t2xAppliA


    # Function for change to Percent
    def transPorc(self, x) -> float:

        return x * 100


# Function to print some arguments on command line

def usage() -> str:
    # argsh = ['']
    return print("Usage ./cdi.py -c [capital] -a [CDI anual] -s [Selic] -i [alíquota IR] -t [taxa CDI] -m [meses] -h [help]")

# class Show


class Show:

    def main(self):
        argv = sys.argv[1:]

        # Using getopt
        try:
            opts, args = getopt.getopt(argv, "c:i:t:a:s:m:h", [
                                       "Capital", "CDI", "Selic", "aliquota IR", "taxa CDI", "meses", "help"])  # "c:a:s:i:t:m:h:"
        except getopt.GetoptError as err:
            # print help information
            print(err)
            sys.exit()

        bf = BFunc()
        # Verifying each options and catching the arguments values
        for opt, arg in opts:
            if opt in ['-c', '--Capital']:
                cap = int(arg)
            elif opt in ['-s', '--Selic']:
                selic = bf.transPorc(float(arg))
            elif opt in ['-a', '--CDI']:
                cdi = float(arg)
                cdiA = bf.transPorc(cdi)   # CDI ao ano
                cdiM = bf.year2month(cdi)  # CDI ao mês
                cdiD = bf.year2day(cdi)    # CDI ao dia
            elif opt in ['-i', '--AliquotaIR']:
                IR = float(arg)
            elif opt in ['-t', '--txCDI']:
                txCDI = float(arg)*1.0
            elif opt in ['-m', '--meses']:
                mes = int(arg)
            elif opt in ['-h', '--help']:
                sys.exit(usage())
            else:
                assert False, "unhandled option"

        # Implementando a ideia de caso não tenha nenhum argumento na linha de
        # comando ao executar o programa, não irá fazer print de nada -> PLUS ULTRA
        if opts == []:
            exit()
        else:

            # Checking if month exists
            if 'mes' in locals():
                mes = int(arg)
            else:
                mes = 1

            # Checking if some args exists
            if ('cap' in locals()) and ('selic' in locals()) and ('txCDI' in locals()) and ('cdiA' in locals()) and ('IR' in locals()):

                print(f'Capital = ${cap}')
                print(f'Taxa Selic = {selic}% ao ano')
                print(
                    f'CDI = {cdiA}% ao ano = {cdiM:.4f}% ao mês = {cdiD:.6f}% ao dia')
                # Verifying which savings value
                # txPoupA is the annual savings amount and txPoupM is the monthly savings amount
                txPoupA = bf.checkAmountSavings(selic)
                txPoupM = BFunc.year2month(self, txPoupA/100.0)
                print(
                    f'Taxa Poup = {txPoupA}% ao ano = {txPoupM:.4f}% ao mês\n')

                RentImp, RentImpA = bf.CDB(cap, cdi, txPoupA, txCDI, IR, mes)
            else:
                print("Valor de argumento está em falta!!!")
                exit(usage())


# Running the program
if __name__ == "__main__":
    s = Show()
    s.main()