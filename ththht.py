import pandas as pd
def read_html_to_dict(html_file):
    tables=pd.read_html(html_file)
    table_dict={}
    for i,table in enumerate(tables):
        table_dict=table.to_dict(orient='list')
        table_dict[f'Table_{i+1}']=table_dict
    return tables_dict
if _name_=='_main_':
    html_file='sample.html'
    result=read_html_to_dict(html_file)
print(result)
