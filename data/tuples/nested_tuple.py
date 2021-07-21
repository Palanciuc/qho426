def steps():
  likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
  return likelihoods

def run():
  s = steps()
  good_steps = []
  bad_steps = []
  for thing in s:
    if thing[1] < 50:
      good_steps.append(thing)
    else:
      bad_steps.append(thing)
  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()