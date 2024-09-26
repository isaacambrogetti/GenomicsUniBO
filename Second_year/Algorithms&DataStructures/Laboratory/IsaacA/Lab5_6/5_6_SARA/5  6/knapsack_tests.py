knapsackInstances = {
  'small': [{ 'capacity': 5.,
              'numberOfItems': 7,
              'sizes': [ 3.1, 1., 2., 1.85, 0.4, 0.3, 0.6 ],
              'utilities': [ 7., 2., 3.9, 3.7, 0.7, 0.5, 1.],
              'bestUtility': 10.7,
              'bestChoice': {0,3} },
            { 'capacity': 375.,
              'numberOfItems': 15,
              'sizes': [ 56.358531, 80.874050, 47.987304, 89.596240, 74.660482, 85.894345, 51.353496,
                         1.498459, 36.445204, 16.589862, 44.569231, 0.466933, 37.788018, 57.118442, 60.716575 ],
              'utilities': [ 0.125126, 19.330424, 58.500931, 35.029145, 82.284005, 17.410810, 71.050142, 30.399487, 
                             9.140294, 14.731285, 98.852504, 11.908322, 0.891140, 53.166295, 60.176397 ],
              'bestUtility': 481.0694,
              'bestChoice': {2, 4, 6, 7, 9, 10, 11, 13, 14} } ],
  'medium': [{ 'capacity': 600.,
               'numberOfItems': 20,
               'sizes': [ 92., 4., 43., 83., 84., 68., 92., 82., 6., 44.,
                          32., 18., 56., 83., 25., 96., 70., 48., 14., 58. ],
               'utilities': [ 44., 46., 90., 72., 91., 40., 75., 35., 8., 54.,
                              78., 40., 77., 15., 61., 17., 75., 29., 75., 63. ],
               'bestUtility': 862.,
               'bestChoice': {1, 2, 4, 6, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19} }],
  'large': [{ 'capacity': 800.,
              'numberOfItems': 100,
              'sizes': [ 485., 326., 248., 421., 322., 795., 43., 845., 955., 252., 9., 901., 122., 94., 738.,
                          574., 715., 882., 367., 984., 299., 433., 682., 72., 874., 138., 856., 145., 995.,
                          529., 199., 277., 97., 719., 242., 107., 122., 70., 98., 600., 645., 267., 972.,
                          895., 213., 748., 487., 923., 29., 674., 540., 554., 467., 46., 710., 553., 191.,
                          724., 730., 988., 90., 340., 549., 196., 865., 678., 570., 936., 722., 651., 123.,
                          431., 508., 585., 853., 642., 992., 725., 286., 812., 859., 663., 88., 179., 187.,
                          619., 261., 846., 192., 261., 514., 886., 530., 849., 294., 799., 391., 330., 298.,
                          790. ],
              'utilities': [ 94., 506., 416., 992., 649., 237., 457., 815., 446., 422., 791., 359., 667., 598.,
                              7., 544., 334., 766., 994., 893., 633., 131., 428., 700., 617., 874., 720., 419.,
                              794., 196., 997., 116., 908., 539., 707., 569., 537., 931., 726., 487., 772., 513.,
                              81., 943., 58., 303., 764., 536., 724., 789., 479., 142., 339., 641., 196., 494.,
                              66., 824., 208., 711., 800., 314., 289., 401., 466., 689., 833., 225., 244., 849.,
                              113., 379., 361., 65., 486., 686., 286., 889., 24., 491., 891., 90., 181., 214., 17.,
                              472., 418., 419., 356., 682., 306., 201., 385., 952., 500., 194., 737., 324., 992.,
                             224. ],
              'bestUtility': 8150.,
              'bestChoice': {32, 37, 6, 38, 10, 13, 48, 53, 23, 25, 60} }]
}




def testKnapsackCorrectness(testCategory):
  from __main__ import solveKnapsack
  failed = False
  
  for instance in knapsackInstances[testCategory]:
    capacity = instance['capacity']
    numberOfItems = instance['numberOfItems']
    sizes = instance['sizes']
    utilities = instance['utilities']
    solution = solveKnapsack(capacity, numberOfItems, sizes, utilities)

    utility = 0.
    size = 0.
    for item in solution:
      utility += utilities[item]
      size += sizes[item]
    
    if size > capacity or abs(utility - instance['bestUtility']) > 0.001:
      if failed:
        print("")
      failed = True
      print ("Test failed:")
      print ("  capacity =", capacity)
      print ("  numberOfItems =", numberOfItems)
      print ("  sizes =", sizes)
      print ("  utilities =", utilities)
      print ("Proposed solution:")
      print ("  choice =", solution)
      print ("  utility =", utility)
      print ("  size =", size)
      print ("Actual solution:")
      print ("  choice =", instance['bestChoice'])
      print ("  utility =", instance['bestUtility'])

  if not failed:
    print ("All tests passed in category:", testCategory)


