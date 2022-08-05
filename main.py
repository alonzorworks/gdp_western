from email.mime import image
import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
#import statsmodels.api as sm
from PIL import Image 
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title = "Home Page",
    page_icon = "🏡"
)

# NOTE Allow pictures to be put into the document. 
def load_lottieurl(url):
    """If the lottie file does not display the image return nothing. This will prevent errors when trying to display the Lottie Files.
    Requires importing packages streamlit_lottie and requests"""
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


def lottie_credit(credit):
    return st.markdown(f"<p style='text-align: center; color: gray;'>{credit}</p>", unsafe_allow_html=True)


df = pd.read_csv("gdp_country.csv")
#df base 100
df_base = pd.read_csv("gdp_country_base.csv")

df_all_c =pd.read_csv("gdp_all_countries.csv")

st.title("Western Countries Analysis 1952-2007 :earth_americas: :earth_asia: :guardsman: ")
world_map = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_b1imuadj.json")
st_lottie(world_map)
lottie_credit("World Sebastian Garcia Taborda Lottie Files")

st.subheader("Analysis for Western Countries")


with st.expander("Click to Read the Analysis"):
    st.write("Interpreting the results of the data using various theoretical academic tenets from various disciplines.")
    st.write("""
Overall, this data is quite elucidating. There are many insights that can be gleaned from the data. For starters, there is a strong correlation between GDP per capita and the life span of a country. The correlation was strong. This suggests that when GDP per capita, the citizens of their respective countries gain access to things that can help extend their life. Likely these come in the form of food and healthcare.

The y-intercept for the linear regression was quite high for the western world 65 years old. The overall y-intercept for the entire planet was 53 years old (including the western countries). However more information about the regression process and the findings are available to read in the last section.

The population was another interesting factor to study. The population of the US was dramatically bigger than any other country studied. The second biggest population studied was Germany, however, the US was over 3 times bigger in terms of population. This may have to do with the landmass of the United States. The US is bigger than the European Union (which comprises most of the western countries) and is only slightly smaller than the European continent. Surprisingly the United States is even bigger than the continent of Australia. However, Australia becomes sparsely populated on its islands because of the inhospitable climate and fewer resources, compelling most of its inhabitants to prefer the coast.

While the United States was the largest population, Israel was growing the fastest. This may be due to how young the country is. The country was established in 1948. In addition to this governments such as the United States gave much age to the state in hopes that it would flourish. Israel is considered the only democracy in the middle east.

There was a weak correlation between GDP and population growth in the western world it was only about 0.31. This is quite weak. This is likely due to sundry factors. For one the western world for the most part is quite developed. Developed nations are further along with the demographic transition model. Less developed societies have a higher birth rate for various reasons. For one agriculture-based wealth makes children an asset, as they can be used as a source of virtually "free" labor while in their parents' household. Religion is more prevalent which promotes conservative family values. Contraception tends not to be available or is frowned upon. Women also tend to have fewer rights, access to education, and work opportunities. The western world is in the later stages of the demographic transition model. Religion dictates the behavior of citizens less in developed socities (even when a large swath of developed populations' still claim affiliation and still find solace in faith). Children are an expensive liability in urban environments. Women are educated and can find work more easily. Women also have more access to birth control and contraceptives. (Educating women is considered to be the best way to curtail population growth according to human geographers and enviornmental scientists). However, note that death rates decreases due to improvements in technology. Societies that started their development later would likely see a higher correlation between the birth rates and GDP. This is because children have not become expensive yet and more cultural values remain intact.

Viewing the base level vs, the regular data was also very interesting. Base level 100 data measured the percentage increase that the country experienced over the first data point available. The raw data plots the points as they are recorded as the data aggregators. From looking at the life expectancy in the Netherlands they seem to be not improving. However, the Netherlands ranked #2 in life expectancy. Higher rankings are harder to marginally improve. In economics this concepts is known as diminishing returns.
""")

st.subheader("Limitations to The Study and The Ambiguity of The Term 'Western'")
with st.expander("Click to See The Limitations of The Data"):
    st.write(f"""
For starters, the data used spans 55 years from 1952- to 2007. It would have been nice to have a wider range of dates. However, this data set was easily accessible on Jupyter Labs and was one of the best datasets on the subject found by the researcher (though there are probably better datasets available that were overlooked). Bear in mind that the range/span of the data is 55 years. The dataset only gives us data for only 12 years within the 55 year range.

\n \n These dates are: {df["year"].unique().tolist()}

The term Western is widely used but means different things depending on who is being talked to. Some would say Western country is any country that is located in the western hemisphere. Others say Western countries are countries that were against the Soviiet Union before it collasped. 

For this study, western countries were classified as primarily Caucasian countries that are amicable diplomatcy-wise in conjunction with obvious historical ties to Europe , that [country] exemplifies democratic values, and Judeo-Christian beliefs while maintaining a capitalistic economy and enjoying a relatively elevated standards of living. These countries should exhibit an enduring reputation of comfort, peace, preeminence, self determination, global importance due to her (the country) attributtes and its affiliation(s) with its powerful constituents.  The foundation of these countries was the European Union and the United States. EU countries were found using a python library called country_groups. The researcher felt it was necessary to include Canada, Israel, and other countries. Countries such as Russia were obviously excluded from the western definition. Japan has some western characteristics but its other attributtes preclude from having the western label. However, some can argue some of the countries in the EU are Eastern. However, if the countries included in the definition are clearly defined, the categorization of the country should not be the most important aspect of the study. Doubtlessly someone can make compelling arguments on why the Western countries included in the dataset is either embellished or incomplete. These 24 countries are considered Western in this project:


Most of the statistics that were done observed the west as an aggregate. Greater insights can be given into countries if they were dissected more individually but that is outside the scope of this study.
\n \n \n {df['country'].unique().tolist()}


There are many other geographic worlds to be explored besides the western one. For example, additional studies can be done on the African continent, Latin America, Arabic/Muslim countries, Asian countries, OPEC countries etc. If one other region were studied here this would allow for greater juxtaposition and insight. However, these regions may be explored in the future in separate projects.


""")


# df = pd.read_csv("gdp_country.csv")
# #df base 100
# df_base = pd.read_csv("gdp_country_base.csv")

# df_all_c =pd.read_csv("gdp_all_countries.csv")
st.header("Charts and Map")
analysis = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_zlrpnoxz.json")
st_lottie(analysis)
lottie_credit("Business Analysis by dhaval on LottieFiles")
df

# Scattergram 
st.subheader("Scattergram of GDP vs Life Expectancy (Population for Size)")
scatter = px.scatter(df, x="lifeExp", y="gdpPercap", color="country", size='gdpPercap', hover_data=['gdpPercap', "lifeExp", "pop"], width = 1000)
st.plotly_chart(scatter)

# Boxplot Prep 
def boxplot(column_name, dframe = df):
    fig = px.box(dframe, x = "country", y = column_name, color = "country", title = f"{column_name} - For Western Countries", width = 1000, height = 500)
    fig.update_layout(xaxis_title = "Country", yaxis_title = f"{column_name}")
    return st.plotly_chart(fig)

# NOTE Graphs Over Time 
#  projection = "natural earth"
def map_chart(column_name):
    world_map = px.scatter_geo(df, locations="iso_alpha", color="country",
                     hover_name="country", size= column_name,
                     animation_frame="year",
                     projection="orthographic", width = 1000 ,height = 600, title = f"{column_name} Over Time - Western Countries")
    return st.plotly_chart(world_map)

def map_chart_flat(column_name):
    world_map = px.scatter_geo(df, locations="iso_alpha", color="country",
                     hover_name="country", size= column_name,
                     animation_frame="year",
                     projection="natural earth", width = 1000 ,height = 600, title = f"{column_name} Over Time - Western Countries")
    return st.plotly_chart(world_map)

# NOTE Start of Maps
st.header("Map Section")

map_chart("gdpPercap")
map_chart("pop")
map_chart("lifeExp")
st.write("The changes in life expectancy is very subtle compared to the other map charts.")

with st.expander("See the flat maps."):
    map_chart_flat("gdpPercap")
    map_chart_flat("pop")
    map_chart_flat("lifeExp")
    st.write("The changes in life expectancy is very subtle compared to the other map charts.")

#with st.expander("Click to See The Boxplots"):

st.subheader("Boxplot Charts")
with st.expander("Click to See The Boxplots"):
    boxplot("lifeExp")
    boxplot("pop")
    boxplot("gdpPercap")


    us_only = df.loc[df["country"] == "United States"]
    exclude_us = df.loc[df["country"] != "United States"]

    st.write("Boxplot for Population US Only and US Excluded")
    boxplot("pop", us_only)
    st.subheader("Boxplots")
    boxplot("pop", exclude_us)



# Mean life expectancy 
country_mean = df.groupby(["country"])["lifeExp"].agg("mean").sort_values(ascending = False)
mean_df = pd.Series.to_frame(country_mean)
mean_df["Rank"] = mean_df["lifeExp"].rank(ascending = False).astype(int)

mean_df["Rank"] = mean_df["Rank"].astype(int)
#mean_df 

# Mean Ranking Function 
def mean_ranking(column_name):
    country_mean = df.groupby(["country"])[column_name].agg("mean").sort_values(ascending = False)
    mean_df = pd.Series.to_frame(country_mean).astype(int)
    mean_df["Rank"] = mean_df[column_name].rank(ascending = False).astype(int)

    mean_df["Rank"] = mean_df["Rank"].astype(int)


    #st.write(f"Ranking of Mean {column_name} for Western Countries")
    with st.expander(f"Click to see Ranking of the Mean {column_name} for Western Countries"):
        return st.table(mean_df)





def median_ranking(column_name):
    country_med = df.groupby(["country"])[column_name].agg("median").sort_values(ascending = False)
    med_df = pd.Series.to_frame(country_med)
    med_df["Rank"] = med_df[column_name].rank(ascending = False).astype(int)

    with st.expander(f"Click to see Ranking of the Median {column_name} for Western Countries"):
        return st.table(med_df) 



# NOTE Ranking Section 

#lifeExp
st.subheader("Life Expectancy Ranked")
mean_ranking("lifeExp")
median_ranking("lifeExp")

#population
st.subheader("Population Ranked")
mean_ranking("pop")
median_ranking("pop")

#GDP Per Capita
st.subheader("GDPPercapita Ranked")
mean_ranking("gdpPercap")
median_ranking("gdpPercap")


# NOTE Boxplot Section

# Boxplot Prep 
def boxplot(column_name, dframe = df):
    fig = px.box(dframe, x = "country", y = column_name, color = "country", title = f"{column_name} - For Western Countries", width = 1000, height = 500)
    fig.update_layout(xaxis_title = "Country", yaxis_title = f"{column_name}")
    return st.plotly_chart(fig)

# NOTE Pannel Data
def pannel_data(column_name):
    fig = px.line(df, x = "year", y = column_name, color = "country", markers = True, width = 1000)
    return st.plotly_chart(fig)

# NOTE Panel Data
st.subheader("Panel Data")
st.write("GDP, Population, and Life Expectancy over time for each country.")
with st.expander("Click here to see GDP, population, and life-expectancy over time"):
    pannel_data("gdpPercap")
    pannel_data("pop")
    pannel_data("lifeExp")

# NOTE Heatmap 
st.subheader("Heatmap")
# heat = plt.figure(figsize = (12, 8))
# sns.set(font_scale = 1.4)
# sns.heatmap(df.iloc[:, 3:6].corr(), annot = True, cmap = "Reds")
# st.pyplot(heat)

heatmap = "heatmap.PNG"
st.image(heatmap, caption = "Heatmap of correlation between variables.")
st.code("""
heat = plt.figure(figsize = (12, 8))
sns.set(font_scale = 1.4)
sns.heatmap(df.iloc[:, 3:6].corr(), annot = True, cmap = "Reds")
st.pyplot(heat)
""")

# NOTE Regression Analysis from Screenshot


# NOTE Base 100 Chart 
# Imported the df in order to avoid issues
west_c = df["country"].unique().tolist()

def base_chart(column_name):
    fig = px.line(df_base, x = "year", y = column_name, color = "country", markers = True, width = 1000)
    st.plotly_chart(fig)

st.subheader("Base One Hundred Charts")

with st.expander("Click to See the Base Charts"):
    st.write("Base 100 helps track the change of a variable in percentage terms.")
    df_base

    base_chart("life_base")
    base_chart("pop_base")
    base_chart("gdp_base")

# NOTE Regression 
st.subheader("Regression (Done in Jupyter Labs)")

st.write("Code Utilized for Regression")

st.code("""
import statsmodels.api as sm
x = sm.add_constant(x)

model = sm.OLS(y, x)

results = model.fit()
results.summary()

""")

st.code("""
# All Nations are included by using df instead of df2 which has been filtered by the EU
# US and other western countries.
x = df["gdpPercap"]
y = df["lifeExp"]

x = sm.add_constant(x)

model = sm.OLS(y, x)

results = model.fit()
results.summary()
""")

west_reg = "regression_western.png"
all_reg = "regression_all_nations.png"
nw_reg = "excluded_west_reg.png"

st.subheader("Regression for Western Countries")
st.write("The equation for western countries is: y (life-expectancy) = 0.0004x + 65.9103")
st.image(west_reg, caption = "Regression Life Expectancy vs. GDP - Western Countries")
st.write("List of western countries:" ,df["country"].unique().tolist())

st.subheader("Regression for All Countries")
st.write("The equation for all countries is: y (life Expectancy)= 0.0008x + 53.9556")
st.image(all_reg, caption = "Regression Life Expectancy vs. GDP All Countries.")
st.write("All countries come from a dataset that includes all of the countries not just western ones.")
st.write(df_all_c["country"].unique().tolist())

st.subheader("Regression for Non-Western Countries (Western Countries Excluded)")
st.write("The equation for Non-western countries. y (life Expectancy) = 0.0007x + 53.2281")
st.image(nw_reg, caption = " Regression for Non-Western countries.")


st.subheader("Analysis of Regression")
st.write("""
From the regression equations we can tell that western countries, tend to have a longer lifespan than their non-western counterparts. People from western countries tend to live over 10 years longer than their non-western counterparts when observing only the y-intercept. \n
Also a dollar in per capita GDP increase, increases the life span of western citizens more on average than it does their non-western counterparts. Succintly that means that wester countries gain more days on earth per dollar, than non-western countriees. \n
Non-Western regression and the regression for all countries have similar values for virtually if not all of the OLS calculation, so those countries do not skew the data in that regard.



""")

circle = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_ax16hsjz.json")
st_lottie(circle)
lottie_credit("Health Analysis loading animation Franz Cyril Locsin")

#Image1 for western
# Image2 for regression for all countries 


# Create a new dataframe for the base calculation 



#with st.expander("Click to See The Boxplots"):

# st.subheader("Boxplot Charts")
# with st.expander("Click to See The Boxplots"):
#     boxplot("lifeExp")
#     boxplot("pop")
#     boxplot("gdpPercap")


#     us_only = df.loc[df["country"] == "United States"]
#     exclude_us = df.loc[df["country"] != "United States"]

#     st.write("Boxplot for Population US Only and US Excluded")
#     boxplot("pop", us_only)
#     st.subheader("Boxplots")
#     boxplot("pop", exclude_us)


