import yfinance as yf
import pandas as pd

print("test")

# 종목별 기간 설정
stocks = {
    "케이씨텍": ("281820.KS", "2023-02-08", "2023-09-25"),
    "MDS테크": ("086960.KQ", "2020-05-27", "2021-04-01")
}

for name, (ticker, start, end) in stocks.items():
    df = yf.download(ticker, start=start, end=end)
    df = df[["Open", "High", "Low", "Close"]]  # 시가, 고가, 저가, 종가만
    df.to_csv(f"{name}.csv", encoding="utf-8-sig")
    print(f"{name} 데이터 저장 완료 ({len(df)}일치) → {name}.csv")
