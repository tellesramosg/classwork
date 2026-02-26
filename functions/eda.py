import pandas as pd

def eda(df: pd.DataFrame) -> None:
    """
    Evaluate basic statistics on a Dataframe
    
    Args:
        df (Pandas.DataFrame): DataFrame to ecaluate
    Returns:
        None
    """
    print(f"{'='*5}DF Shape: {df.shape}{'='*5}")
    num_cols = []
    cat_cols = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            num_cols.append(col)
        else:
            cat_cols.append(col)
            
    print(f"{'*'*3}Numeric Columns{'*'*3}")
    for col in num_cols:
        n_min = df[col].min()
        n_max = df[col].max()
        num_na = df[col].isna().sum()
        print(col)
        print(f"\tNum NA: {num_na}")
        print(f"\t% NA: {(num_na / len(df)) * 100}%")
        print(f"\tMin: {n_min}")
        print(f"\tMax: {n_max}")
        print(f"\tRange: {n_max - n_min}")
        print(f"\t25%: {df[col].quantile(0.25)}")
        print(f"\t75%: {df[col].quantile(0.75)}")
        print(f"\tSt. Dev.: {df[col].std()}")
        print(f"\tNum unique: {df[col].nunique()}")
    print("\n")
    print(f"{'*'*3}CATEGORICAL COLS{'*'*3}")
    for col in cat_cols:
        d = df[col]
        num_null = d.isna().sum()
        print(f"{col}")
        print(f"\tNum NA: {num_null}")
        print(f"\t% NA: {(num_null / len(df)) * 100}%")
        print(f"\tNum Uniques: {d.nunique()}")
        if d.nunique() < 7:
            print(f"Unique Vals: {d.unique()}")