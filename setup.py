import rpy2.robjects as ro
import rpy2.robjects as robjects


def main():
    robjects.r("""
        Sys.setlocale("LC_ALL", "ja_JP.SJIS")
    """)
    robjects.r["load"]("input/.RData")
    objs = robjects.r["ls"]()
    for obj_name in objs:
        # RでデータフレームをCSVに書き出す
        ro.r(f'write.csv({obj_name}, file="input/{obj_name}.csv", row.names=FALSE, fileEncoding="UTF-8")')


if __name__ == '__main__':
    main()
