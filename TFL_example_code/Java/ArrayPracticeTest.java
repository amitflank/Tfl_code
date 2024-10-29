
public class ArrayPracticeTest {

    public static void main(String[] args) {
        testSumArray();
        testCountCharOccurrences();
        testFindLongestString();
        testReverseArray();
        testCountWordsOfLength();
        testCountVowels();
        testFindMinAndMax();
        testCountElementOccurrences();
    }

    private static void testSumArray() {
        int[] arr = {3, 7, 1, 9};
        int expected = 20;
        int result = ArrayPractice.sumArray(arr);
        printTestResult("sumArray", result, expected);
    }

    private static void testCountCharOccurrences() {
        char[] arr = {'a', 'b', 'a', 'c', 'd'};
        char target = 'a';
        int expected = 2;
        int result = ArrayPractice.countCharOccurrences(arr, target);
        printTestResult("countCharOccurrences", result, expected);
    }

    private static void testFindLongestString() {
        String[] arr = {"apple", "banana", "pear", "grapefruit"};
        String expected = "grapefruit";
        String result = ArrayPractice.findLongestString(arr);
        printTestResult("findLongestString", result, expected);
    }

    private static void testReverseArray() {
        int[] arr = {1, 2, 3, 4, 5};
        int[] expected = {5, 4, 3, 2, 1};
        ArrayPractice.reverseArray(arr);
        printTestResult("reverseArray", arr, expected);
    }

    private static void testCountWordsOfLength() {
        String[] arr = {"apple", "kiwi", "banana", "fig", "peach"};
        int length = 5;
        int expected = 2;
        int result = ArrayPractice.countWordsOfLength(arr, length);
        printTestResult("countWordsOfLength", result, expected);
    }

    private static void testCountVowels() {
        String sentence = "hello world";
        int expected = 3;
        int result = ArrayPractice.countVowels(sentence);
        printTestResult("countVowels", result, expected);
    }

    private static void testFindMinAndMax() {
        int[] arr = {4, 7, 2, 8, 5};
        int[] expected = {2, 8};
        int[] result = ArrayPractice.findMinAndMax(arr);
        printTestResult("findMinAndMax", result, expected);
    }

    private static void testCountElementOccurrences() {
        int[] arr = {1, 2, 2, 3, 3, 3};
        String expected = "1 appears 1 time, 2 appears 2 times, 3 appears 3 times";
        String result = ArrayPractice.countElementOccurrences(arr);
        printTestResult("countElementOccurrences", result, expected);
    }

    private static void printTestResult(String testName, Object result, Object expected) {
        System.out.println(testName + ": ");
        System.out.println("  Expected: " + expected);
        System.out.println("  Received: " + result);
        System.out.println(result.equals(expected) ? "  PASS\n" : "  FAIL\n");
    }

    private static void printTestResult(String testName, int[] result, int[] expected) {
        boolean pass = java.util.Arrays.equals(result, expected);
        System.out.println(testName + ": ");
        System.out.println("  Expected: " + java.util.Arrays.toString(expected));
        System.out.println("  Received: " + java.util.Arrays.toString(result));
        System.out.println(pass ? "  PASS\n" : "  FAIL\n");
    }
}