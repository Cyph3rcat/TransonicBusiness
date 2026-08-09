"""Regenerate every figure in report/figures/ from the source data."""
import ch1_3, ch5_6, ch7_10, ch11, threeview

if __name__ == "__main__":
    print("three-view:")
    threeview.three_view()
    print("chapters 1-3:")
    for f in (ch1_3.fig_1_1, ch1_3.fig_2_1, ch1_3.fig_3_1, ch1_3.fig_3_2,
              ch1_3.fig_3_3):
        f()
    print("chapters 5-6:")
    for f in (ch5_6.fig_5_0, ch5_6.fig_5_1, ch5_6.fig_5_2, ch5_6.fig_5_3,
              ch5_6.fig_5_4, ch5_6.fig_6_1, ch5_6.fig_6_2):
        f()
    print("chapters 7-10:")
    for f in (ch7_10.fig_7_1, ch7_10.fig_8_1, ch7_10.fig_8_2, ch7_10.fig_9_1,
              ch7_10.fig_9_2, ch7_10.fig_9_3, ch7_10.fig_10_1,
              ch7_10.fig_10_2, ch7_10.fig_10_3):
        f()
    print("chapter 11:")
    for f in (ch11.fig_11_1, ch11.fig_11_2, ch11.fig_11_3):
        f()
    print("done.")
