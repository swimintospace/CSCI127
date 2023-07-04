


follows = int(input("Enter amount of social media followers: "))
influence = ""

if follows < 0:
    influence = "Error"
elif follows < 1000:
    influence = "Hyper Influencer"
elif follows < 10000:
    influence = "Nano Influencer"
elif follows < 100000:
    influence = "Micro Influencer"
elif follows < 500000: 
    influence = "Mid-Tier Influencer"
elif follows < 1000000:
    influence = "Macro Influencer"
else:
    influence = "Celebrity Influencer"

print("Your influencer tier is:", influence)