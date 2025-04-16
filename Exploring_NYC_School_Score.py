import pandas as pd
schools = pd.read_csv("schools.csv")
schools.head()

# Which NY schools have the best maths results?
df_schools = pd.DataFrame(schools)
# DataFrame with the school_name, average_math (sorted values)
best_math_schools = df_schools[df_schools["average_math"] > 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)
print("List of the schools with the best maths results", best_math_schools)

# What are the top 10 performing schools based on the combined SAT scores?
# Sum of the total results of the differents schools
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10)
print("The top 10 performing schools based on the combined SAT scores", top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?
# the name of the NYC borough with the largest standard deviation of "total_SAT"
borough = schools.groupby("borough")["total_SAT"].std().round(2).to_dict()
print("List of the name of the NYC borough with the largest standard deviation of total_SAT \n",borough)
print("=> As we can see here, Manhattan has the largest deviation of total_SAT : 230.29 \n")

# the number of schools in the borough.
print("How many schools are there in Manhattan?")
num_schools = schools.groupby("borough")["school_name"].count().round(2).to_dict()
print(num_schools)
num_schools_Man = schools.groupby("borough")["school_name"].count()["Manhattan"]
print(f"there are {num_schools_Man} schools in Manhattan \n")

# the mean of "total_SAT"
average_SAT = schools.groupby("borough")["total_SAT"].mean()["Manhattan"].round(2)
print("The mean of total_SAT :" ,average_SAT,"\n")

# the standard deviation of "total_SAT"
std_SAT = schools.groupby("borough")["total_SAT"].std()["Manhattan"].round(2)
print("The standard deviation of total_SAT :", std_SAT, "\n")

# Create a DataFrame
largest_std = {
    "borough":["Manhattan"],
    "num_schools": [num_schools_Man],
    "average_SAT": [average_SAT],
    "std_SAT": [std_SAT]
} 
largest_std_dev = pd.DataFrame(largest_std)
print(largest_std_dev)
