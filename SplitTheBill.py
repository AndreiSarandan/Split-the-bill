
def split_the_bill(x):
    li = list(x.values())
    ld = []
    lc = list(x.keys())
    average = sum(li)/len(li)
    for item in li:
        ld.append(float("{:.2f}".format(item-average)))
    return dict(zip(lc, ld))


group = {'VzlilaHQEOu': 344155.5714285714, 'BDTvAztlDDsP': 41026.57142857142, 'VTddDslmiu': -208066.42857142858, 'OVjTGUPtTrdC': -
         219930.42857142858, 'yHopqgGRJJoJBMvbqfZ': 271788.5714285714, 'WeEjlocCZRD': -236156.42857142858, 'ch': 7182.57142857142}
print(split_the_bill(group))
