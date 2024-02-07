# JMESPath-Rules

# The Zen of Security Rules
- almost all points from the Zen of Python are applicable to security rules - start there
- favor inclusion-by-exception over exclusion-by-exception, or else endure perpetual whack-a-mole
- have a propensity towards performance; expensive rules must justify the cost
- resist temptation to over or under-scoping; balance is key
- generic patterns can minimize brittleness, but at the cost of performance
- correlation is powerful, but overly comprehensive rules can lead to brittleness and trivial bypasses
- detect behaviors over IOCs, except when necessary
- if a rule is too complex to understand, the alert is even worse
- just like code, readability is important for avoiding errors
- detection logic formatting should emphasize logical precedence and grouping
- detection logic should be resilient, but when it can’t, use multiple rules
- consistency in rule structure leads to predictability and fewer errors
- if you can detect it, you can test it
- always version your rules
- maintenance cost of a rule should not outweigh the value of the rule
- there will ALWAYS be surprises from FPs and FNs
- minimizing FPs sometimes outweighs eliminating FNs, due the costs of alert fatigue
- less is more; don’t write rules for the sake of writing rules
- there is no “correct” quantity of total rules, but there can be too many and too few
- when necessary, break the rules, so you don’t break the rules
- production environments vary wildly, so minimize assumptions
- adopt a detections-as-code or similar software-driven process for managing rules early

  *from: https://br0k3nlab.com/resources/zen-of-security-rules/*
