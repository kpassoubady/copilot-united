# Hallucination Hunter 🐛 (Critical Review)

## The Challenge: The Thread-Safety Trap.

Here is the code:
```java
public class DateUtil {
    // Copilot suggests this 'optimization' to avoid creating instances
    private static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");

    public static Date parse(String dateStr) throws ParseException {
        return sdf.parse(dateStr);
    }
}
```

## The Goal 

Students must use Copilot Chat to ask, "Is this code has a bug/thread-safety issue?" or write a unit test to expose the bug. 
