# explore.py has functions that can be used to do
# an exploratory data analysis of calcium imaging
# data
#
# created by: Daniel Schuette (github.com/DanielSchuette/)
# License: MIT
import pandas as pd


def calc_response_rate(df, threshold=1.2, utp_range=(40, 480),
                       verbose=False, plot=False):
    """
    this function calculates the response rate for calcium imaging data sets
    it takes a pandas.io.excel.ExcelFile and iterates over all data sheets and
    columns in the input data frames

    ------------------------------
    arguments:
    df        - input data (pandas.io.excel.ExcelFile)
    threshold - defaults to 1.2, the response threshold for your dataset
    utp_range - defaults to (40,480)
                a tuple indicating the range in which to look
    verbose   - defaults to False,
                is True, verbose output is printed
                (use it to suppress output)
    plot      - defaults to False,
                if True, plot boxplots to visualize computations
    """
    sheetnames = df.sheet_names.copy()
    sheetnames.sort()
    counter = 0
    col_counter = 0
    appended_data = []
    for sheetname in sheetnames:
        # print("this is a new sheet: {}".format(sheetname))
        selected_df = pd.read_excel(df, sheetname)[utp_range[0]:utp_range[1]]
        selected_df_max = selected_df.max()

        # counter in 1st but not 2nd loop so it's reset to 0 after every sheet
        # but not after every column
        counter = 0
        col_counter = 0
        for idx in selected_df_max.index:
            col_counter += 1
            if selected_df_max[idx] >= threshold:
                pass
                # TODO: implement actual functionality
                # print("current idx: {}".format(idx))
                # print(utp_max[idx])
            else:
                counter += 1

        d = {'Sheet name': [sheetname],
             'Total cells': [col_counter],
             'Non-responding': [counter],
             'Percentage responding': [100-(counter*100/col_counter)]}
        data = pd.DataFrame(d)
        appended_data.append(data)
    appended_data = pd.concat(appended_data, ignore_index=True)
    if verbose:
        print(appended_data)
    if plot:
        appended_data.loc[0:5].boxplot()
        appended_data.loc[6:12].boxplot()
    if verbose:
        print('Statistics for control cells')
        print(appended_data.loc[0:5].mean())
        print('Statistics for L89A cells')
        print(appended_data.loc[6:12].mean())
