from re import X
import streamlit as st
import numpy as np
import pandas as pd

st.title("CALPLOT")

df = []


graph_type = st.selectbox(
    label="プロットタイプを選択",
    options=["ラインチャート", "エリアチャート", "棒グラフ"],
    index=0,
    key=None,
    help=None,
    on_change=None,
    args=None,
    kwargs=None,
    disabled=False,
)

# 軸ラベルを追加したいけど今のとこ解決策がないみたい
xlabel = st.text_input("x軸ラベルを入力してください", placeholder="時間[s]")
ylabel = st.text_input("y軸ラベルを入力してください", placeholder="距離[m]")


class DrawData(object):
    def ready(self, matrix):
        self.matrix = matrix
        df = pd.DataFrame(self.matrix, columns=["a", "b", "c"])
        self.df = df

    def line_chart(self):
        st.line_chart(data=self.df, use_container_width=True, x=[np.random.rand(20, 1)])

    def area_chart(self):
        st.area_chart(data=self.df, use_container_width=True, x=[np.random.rand(20, 1)])

    def bar_chart(self):
        st.bar_chart(data=self.df, use_container_width=True, x=[np.random.rand(20, 1)])


target = DrawData()
target.ready(np.random.rand(20, 3))

st.write(f"横軸: {xlabel}", f"縦軸: {ylabel}")


if graph_type == "ラインチャート":
    target.line_chart()
elif graph_type == "エリアチャート":
    target.area_chart()
elif graph_type == "棒グラフ":
    target.bar_chart()
