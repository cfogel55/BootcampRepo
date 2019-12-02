import pandas as pd
import numpy as np

file_to_load = "purchase_data.csv"
purchase_data = pd.read_csv(file_to_load)
#print(purchase_data.head())

# #Player Count
# total_players = purchase_data.SN.nunique() #players are in data set multiple times
# total_players_series = pd.Series({"Total Players": total_players})
# #print(total_players_series)

#Purchasing Analysis (total)
#Number of unique items
num_unique_items = purchase_data['Item Name'].nunique()

#Avg Purchase Price
avg_purchase_price = purchase_data.Price.mean()

# #Total Number of Purchases
num_purchases = purchase_data['Purchase ID'].count()

# #Total Revenue
total_revenue = purchase_data.Price.sum()

purchasing_analysis_df = pd.Series({
    "Number of Unique Items": num_unique_items, 
    "Average Price": avg_purchase_price, 
    "Number of Purchases:": num_purchases,
    "Total Revenue:": total_revenue})

print(purchasing_analysis_df)

# #Percentage and count of players
# gender_count = purchase_data.groupby('Gender').SN.nunique() #same SN in file multiple times due to multiple purchases
# gender_perc = round(gender_count / total_players * 100,2)

# gdf = pd.DataFrame({"Total Count":gender_count, "Percentage of Players":gender_perc})
# #print(gdf)

# #Purchases by SN
# num_purchasers = purchase_data.SN.nunique()
# #print(num_purchasers)

#Purchasing Analysis (By Gender)
# purchase_count_per_gender = purchase_data.groupby("Gender")['Purchase ID'].count()
# num_persons_per_gender = purchase_data.groupby("Gender").SN.nunique()
# avg_purchase_price_per_gender = purchase_data.groupby("Gender").Price.mean()
# total_purchase_value_per_gender = purchase_data.groupby("Gender").Price.sum()
# avg_purchase_per_person_per_gender = total_purchase_value_per_gender / num_persons_per_gender

# gdf = pd.DataFrame({
#     "Purchase Count": purchase_count_per_gender, 
#     "Average Purchase Price": round(avg_purchase_price_per_gender,2),
#     "Total Purchase Value": total_purchase_value_per_gender,
#     "Avg Total Purchase per Person": avg_purchase_per_person_per_gender})
# print(gdf)

# #Age Demographics
# max_age = purchase_data.Age.max()

# #Deterine number of bins needed. Divide by 5-year groupings. Subtract 9 for first group 0 - 9 years old.
# num_bins = (max_age - 9) / 5

# #If division by 5 returns a remainder, need an additional bin for that 0.xx person.
# if num_bins % 5 != 0:
#     num_bins += 1

# #Create bins_list containing upper ages of age ranges.
# #Create labels_lists containing age ranges.
# bins_list = [0, 9] #accounting for first range < 10 years old
# labels_list = ["<10"]
# upper_bin_age = 9
# for i in range(int(num_bins)):
#     upper_bin_age += 5
#     bins_list.append(upper_bin_age)
#     labels_list.append(str(upper_bin_age - 4) + "-" + str(upper_bin_age))

# #create new column 'age_bin'
# purchase_data['age_bin'] = pd.cut(purchase_data['Age'], bins=bins_list, labels=labels_list)

# purchase_count_by_age_bin = purchase_data.groupby('age_bin').Price.count()
# num_persons_in_age_bin = purchase_data.groupby('age_bin').SN.nunique()
# avg_purchase_price_by_age_bin = purchase_data.groupby('age_bin').Price.mean()
# total_purchases_by_age_bin = purchase_data.groupby('age_bin').Price.sum()
# avg_purchase_per_person_by_age_bin = total_purchases_by_age_bin / num_persons_in_age_bin

# age_demographics_df = pd.DataFrame ({
#     "Purchase Count": purchase_count_by_age_bin,
#     "Average Purchase Price": avg_purchase_price_by_age_bin,
#     "Total Purchase Value": total_purchases_by_age_bin,
#     "Average Purchase Total Per Person": avg_purchase_per_person_by_age_bin
# })
# #print(age_demographics_df)

# #Top Spenders


# #Most Popular Items
# #create new data frame from purchase_data
# most_popular_df= pd.DataFrame(purchase_data)

# # most_popular_df = pd.DataFrame(purchase_data.groupby(['Item ID', 'Item Name', 'Price'])['Item ID'].count().nlargest(5))
# most_popular_itemcount= purchase_data.groupby('Item ID')['Purchase ID'].count()
# most_popular_price= purchase_data.groupby('Item ID')['Price'].sum()
# most_popular_price= purchase_data.groupby('Item ID')['Price'].sum()

# most_popular_df['Total Purchase Value'] = most_popular_df['Price'] * most_popular_df['Item Count']
# print(most_popular_df.head(10)
# most_popular_itemcount =purchase_data.groupby('Item ID')['Item ID'].count()

# # for a, b, c, d in most_popular_df:
# #     print (a, b, c, d)
# print(most_popular_df)

# # for value, a in most_popular_df['Item ID'].value_counts().iteritems():
# #     print(value, a)
# #print(most_popular_df)

