import pandas as pd
import matplotlib.pyplot as plt
def plots_configs():

    #plt.style.use('ggplot')
    plt.rcParams.update({'figure.facecolor': (1.0, 1.0, 0.80, 0.15)})
    
    plt.rcParams['figure.figsize'] = (8, 4)
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    #plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.grid'] = False
    plt.rcParams['font.size'] = 13
    pd.options.display.max_columns = None
    #plt.rcParams['font.sans-serif'] = 'Serif'
    pd.set_option('display.expand_frame_repr', False)



def pie_bar_plot(data, var, title='', labels_col=''):
    
    # Pie Plot
    prop = pd.DataFrame(data[var].value_counts()).reset_index()
    colors = sns.color_palette('Set2')[0:2]
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    ax[0].pie(prop['count'], labels=prop[labels_col], autopct='%.3f%%' , explode=[0.01, 0.01], colors=colors)
    ax[0].set_title(f'{title}')
    ax[0].legend()

    # Count Bar Plot
    bar = ax[1].bar(x=prop[labels_col], height=prop['count'], color=colors)
    plt.bar_label(bar, fmt='{:,.2f}')
    ax[1].set_title(f'{title}')
    ax[1].set_ylabel(f'Quantity')
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['left'].set_visible(False)
    ax[1].set_yticks([])


def stats_table(df):

    """This function receives a dataframe and returns a dataframe with summary statistics.

    Args:
        df (DataFrame): Dataset.

    Returns:
        DataFrame: Table with summary statistics.
    """

    num_att = df.select_dtypes(exclude=['object', 'datetime64[ns]'])

    return num_att.agg(['min', 'max', 'ptp', 'median', 'mean', 'std', 'var', 'skew', 'kurtosis']).T.reset_index().rename(columns={'ptp': 'range', 'index': 'attributes'})


def dataset_shape(data: pd.DataFrame, name=''):
    
    print(f'{name} Number of rows: {data.shape[0]:,}')
    print(f'{name} Number Columns: {data.shape[1]}')


def sum_table(df_):

    """This function receives a dataset and returns a dataframe with information about each column of the dataset.
    Args:
        df_ (DataFrame): Dataset.

    Returns:
        DataFrame: returns a dataframe with the number of unique values and missing value of each column of a dataset.
    """

    summary = df_.dtypes.to_frame().rename(columns={0: 'dtypes'})
    summary['Uniques'] = df_.nunique()
    summary['Missing'] = df_.isnull().sum()
    summary['Missing %'] = np.round((df_.isnull().sum()/len(df_)).values*100, 2)
    summary = summary.reset_index().rename(columns={'index': 'Name'})

    memory_usage = df_.memory_usage(index=False).sum()/1_000_000
    print(f'Memory Usage: {memory_usage:.2f} MB')
    return summary