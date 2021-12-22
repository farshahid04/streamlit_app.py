import pandas as pd
import streamlit as st
import numpy as np
import time


hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')

outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

print ('hospital_info:' , len(hospitaldf))


print ('outpatient_info:' , len(outpatientdf))


print ('inpatient_info:' , len(inpatientdf))

st.title('STREAMLIT APP DEPLOYMENT')
st.write('Welcome, *Everyone!* :sunglasses:')

def load_hospitals(allow_input_mutation=True):
    df_hospital_1 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_1


def load_inatpatient(allow_input_mutation=True):
    df_inpatient_1 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_1


def load_outpatient(allow_input_mutation=True):
    df_outpatient_1= pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return df_outpatient_1


    
# FAKE LOADER BAR TO STIMULATE LOADING    
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)



# Load the data:     
df_hospital_1 = load_hospitals()
df_inpatient_1 = load_inatpatient()
df_outpatient_1 = load_outpatient()

# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(df_hospital_1)

st.header('Outpatient Data Preview')
st.dataframe(df_outpatient_1)

st.header('Inpatient Data Preview')
st.dataframe(df_inpatient_1)


#Bar Chart
st.subheader('Hospital Type in New York')
st.bar1 = df_hospital_1['hospital_type'].value_counts().reset_index()
st.dataframe(st.bar1)
st.caption('Acute care hospitals is the most common hospital type in New York ')

st.subheader('Visual Representation of hospital types:')
st.fig = px.pie(st.bar1, values='hospital_type', names='index')
st.plotly_chart(fig)
st.caption('Different hospital types in the New York Area above, with acute care hospitals taking a huge chunk')

#Timeliness of Care
ny_hospitals = df_hospital_1[df_hospital_1['state'] == 'NY']

nc_hospitals = df_hospital_1[df_hospital_1['state'] == 'NC']


st.subheader('NY Hospitals - Timeliness of Care')
bar2 = ny_hospitals['timeliness_of_care_national_comparison'].value_counts().reset_index()
fig2 = px.bar(bar2, x='index', y='timeliness_of_care_national_comparison')
st.plotly_chart(fig2)
st.caption('Majority of hospitals in the NY area fall below the national\
        average as it relates to timeliness of care')

st.subheader('NC Hospitals - Timeliness of Care')
bar4 = nc_hospitals['timeliness_of_care_national_comparison'].value_counts().reset_index()
fig5 = px.bar(bar4, x='index', y='timeliness_of_care_national_comparison')
st.plotly_chart(fig5)
st.caption('Based on the bar chart above, we can see the the timeliness\
           of care data for the majority of hospitals in the North Carolina area \
               is the same as the national average and a little bit below the national average')



st.markdown('1. What are the most common hospital types and where does New York rank in regards to timeliness of care?')
st.markdown('- As shown by the analysis above, the most common hospital type in NY is acute care (144 acute care hospitals).\
            In terms of ranking, most of the New York Hospitals are below national average in regards to timeliness of care')  

##INPATIENT and OUTPATIENT 
st.title('Inpatient and outpatient dataframes')
st.markdown('The dataframe displayed below is for the Inpatient facility')

st.subheader('Inpatient Facility')
bar7 = df_inpatient_1['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Bar Chart of Inpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)


st.markdown('The dataframe displayed below is for the outpatient facility')

st.subheader('Outpatient Facility')
bar7 = df_outpatient_1['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Bar Chart of outpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)

st.markdown('2.  Which states have the greatest number of inpatient and outpatient facilities?')
st.markdown('- As shown by the analysis above, Florida has the most inpatient facilities and Texas has the most outpatient facilities') 


##Common D/C 


common_discharges = df_inpatient_1.groupby('drg_definition')['total_discharges'].sum().reset_index()


top10 = common_discharges.head(10)
bottom10 = common_discharges.tail(10)



st.subheader('DRGs')
st.dataframe(common_discharges)


col1, col2 = st.columns(2)

col1.subheader('Top 10 DRGs')
col1.dataframe(top10)

col2.subheader('Bottom 10 DRGs')
col2.dataframe(bottom10)

st.markdown('3. What is Stony Brooks top three and bottom three inpatient DRG service?')
st.markdown('- As shown by the analysis above, the top 3 are heart transplant, ecmo, and t rach\
                while the bottom 3 are trauma related, hiv related conditions') 



st.header('Merging of Hospital and Inpatient data sets')
df_hospital_1['provider_id'] = df_hospital_1['provider_id'].astype(str)
df_inpatient_1['provider_id'] = df_inpatient_1['provider_id'].astype(str)
df_merged2 = df_inpatient_1.merge(df_hospital_1, how='left', left_on='provider_id', right_on='provider_id')
df_merged_clean2 = df_merged2[df_merged2['hospital_name'].notna()]
df_merged_clean_SB2 = df_merged_clean2[df_merged_clean2['provider_id'] == '330239']
df_merged_clean_SB2

st.header('Pivot table (avg total cost of each DRG for SBU Hospital)')
st.subheader('Pivot DRG for SBU Hospital')
dataframe_pivot = df_merged_clean_SB2.pivot_table(index=['provider_name','drg_definition'],values=['average_total_payments'],aggfunc='mean')
st.dataframe(dataframe_pivot)

##APC
st.markdown('Merging of Datasets to show SBU Hospital values')
df_hospital_1['provider_id'] = df_hospital_1['provider_id'].astype(str)
df_outpatient_1['provider_id'] = df_outpatient_1['provider_id'].astype(str)
df_merged = df_outpatient_1.merge(df_hospital_1, how='left', left_on='provider_id', right_on='provider_id')

st.dataframe(df_merged)
st.markdown('Cleaning of df_merge')
df_merged_clean = df_merged[df_merged['hospital_name'].notna()]
st.dataframe(df_merged_clean)
st.header('Stony Brook University Hospital dataset')
df_merged_clean_SB = df_merged_clean[df_merged_clean['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
df_merged_clean_SB


st.subheader('Pivot APC for SBU Hospital')
dataframe_pivot = df_merged_clean_SB.pivot_table(index=['provider_id','apc'],values=['average_total_payments'],aggfunc='mean')
st.dataframe(dataframe_pivot)
st.markdown('4. What are the top 3 expensive APC for SBU Hopsital?')
st.markdown('The most expensive average total cost for APC in the outpatient and hospital dataframe are Level IV endoscopy 2307.21, \
             Level IV Nerver Injections 1325.64 and the third is Level II Cardiac Imaging 1300.67')


## Comparison

st.header('Merging datasets for SBU and St. Charles Hospital')
st.markdown('Merging of Datasets to show SBU Hospital values')
df_hospital_1['provider_id'] = df_hospital_1['provider_id'].astype(str)
df_outpatient_1['provider_id'] = df_outpatient_1['provider_id'].astype(str)
df_merged = df_outpatient_1.merge(df_hospital_1, how='left', left_on='provider_id', right_on='provider_id')

st.dataframe(df_merged)
st.markdown('Cleaning of df_merge')
df_merged_clean = df_merged[df_merged['hospital_name'].notna()]
st.dataframe(df_merged_clean)

st.header('Stony Brook University Hospital dataset')
df_merged_clean_SB = df_merged_clean[df_merged_clean['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
df_merged_clean_SB

st.header('St Charles')
df_merged_clean_STC = df_merged_clean[df_merged_clean['hospital_name'] == 'ST CHARLES HOSPITAL']
df_merged_clean_STC

st.header('Comparison of St Charles and SBU Hospitals')
final_df_comparison = pd.concat([df_merged_clean_STC, df_merged_clean_SB])
st.dataframe(final_df_comparison)

st.subheader('Final Comparison Pivot Table')
dataframe_pivot = final_df_comparison.pivot_table(index=['hospital_name','apc'],values=['average_total_payments'],aggfunc='mean')
st.dataframe(dataframe_pivot)

bar2 = final_df_comparison['hospital_name'].value_counts().reset_index()
st.subheader('Bar chart displaying SBU and St Charles differences between average total payments')
fig3 = px.bar(bar2, x='index', y='hospital_name')
st.plotly_chart(fig3)
st.dataframe(bar2)

st.markdown('5. What is the difference between the total payment of Stony Brook Hospital compared to st. charles hospital?')
st.markdown('- As shown by the analysis, we can see Stony Brook Hospital has a significantly higher cost of average total payments with Endoscopy upper airway ranking the highest compared to St Charles hospital')




##Mortality rates
st.header('Mortality Rates of NY and NC hospitals')
st.subheader('NY Hospitals - Mortality Rate')
bar2 = ny_hospitals['mortality_national_comparison'].value_counts().reset_index()
fig2 = px.bar(bar2, x='index', y='mortality_national_comparison')
st.plotly_chart(fig2)


st.subheader('NC Hospitals - Mortality Rate')
bar4 = nc_hospitals['mortality_national_comparison'].value_counts().reset_index()
fig5 = px.bar(bar4, x='index', y='mortality_national_comparison')
st.plotly_chart(fig5)

st.markdown('6. How does New Yorks mortality rate compare with North Carolinas mortality rate?')
st.markdown('- Based on the bar charts above, we can see the mortality rate is 60% for NC hospitals and close to 100%\
           for NY hospitals, both remaining around the same as the national average')

