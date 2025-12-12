# The "Prompt Whisperer" Mystery 🕵️ (Prompt Engineering)
The Challenge: Reverse-engineer a complex Java Stream.

## The Setup
Here is the code:

```java
Map<String, Long> result = transactions.stream()
    .filter(t -> t.getAmount() > 1000)
    .collect(Collectors.groupingBy(Transaction::getCurrency, Collectors.counting()));
```

## The Goal
Students must write a natural language prompt that gets Copilot to output this exact stream pipeline on the first try.