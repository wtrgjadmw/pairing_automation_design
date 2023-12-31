from export_formula.fp12 import fp12_mul, fp12_conj, fp12_frob, fp12_sqr
from export_formula.ep2 import ep2_add, ep2_dbl, fp12_sparse_d6, fp12_sparse_m6, fp12_SQR012345
from export_formula.fp24 import fp24_mul, fp24_conj, fp24_frob, fp24_sqr
from export_formula.ep4 import ep4_add, ep4_dbl, fp24_sparse_d6, fp24_sparse_m6, fp24_SQR012345
from export_formula.transform import FormulaOrganizer
from lib.parameters import curve_group, curve_name
import os


def printCsv(filename, formulaList):
    write_f = open(filename, 'w')
    organizer = FormulaOrganizer()
    formulaList = organizer.remove_extra_formula(formulaList)
    for formula in formulaList:
        write_f.write("{},{},{},{}\n".format(
            formula.ret, formula.opr1, formula.opr2, formula.type))


def fp12_makeCsv(directory: str):
    os.makedirs(directory, exist_ok=True)
    printCsv(directory+"CONJ.csv", fp12_conj("a", "c"))
    printCsv(directory+"FROB.csv", fp12_frob("a", "c"))
    printCsv(directory+"MUL.csv", fp12_mul("a", "b", "c"))
    printCsv(directory+"SQR.csv", fp12_sqr("a", "c"))
    printCsv(directory+"PDBL.csv", ep2_dbl())
    printCsv(directory+"PADD.csv", ep2_add())
    printCsv(directory+"SQR012345.csv", fp12_SQR012345("a", "c"))
    printCsv(directory+"SPARSE_D.csv", fp12_sparse_d6("a", "b", "c"))
    printCsv(directory+"SPARSE_M.csv", fp12_sparse_m6("a", "b", "c"))


def fp24_makeCsv(directory: str):
    os.makedirs(directory, exist_ok=True)
    printCsv(directory+"CONJ.csv", fp24_conj("a", "c"))
    printCsv(directory+"FROB.csv", fp24_frob("a", "c"))
    printCsv(directory+"MUL.csv", fp24_mul("a", "b", "c"))
    printCsv(directory+"SQR.csv", fp24_sqr("a", "c"))
    printCsv(directory+"PDBL.csv", ep4_dbl())
    printCsv(directory+"PADD.csv", ep4_add())
    printCsv(directory+"SQR012345.csv", fp24_SQR012345("a", "c"))
    printCsv(directory+"SPARSE_D.csv", fp24_sparse_d6("a", "b", "c"))
    printCsv(directory+"SPARSE_M.csv", fp24_sparse_m6("a", "b", "c"))


if __name__ == "__main__":
    if curve_group == "bls12":
        fp12_makeCsv(
            "/home/mfukuda/pairing_automation_design/csv/{}/{}/".format(curve_group, curve_name))
    elif curve_group == "bls24":
        fp24_makeCsv(
            "/home/mfukuda/pairing_automation_design/csv/{}/{}/".format(curve_group, curve_name))
