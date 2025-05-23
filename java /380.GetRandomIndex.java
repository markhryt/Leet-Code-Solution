import java.util.HashMap;
import java.util.ArrayList;
import java.util.Random;


class RandomizedSet {
    HashMap<Integer, Integer> theMap;
    ArrayList<Integer> theArr;


    public RandomizedSet() {
        theMap = new HashMap<>();
        theArr = new ArrayList<>();
    }

    public boolean insert(int val) {
        if(theMap.containsKey(val)){
            return false;
        }
        theMap.put(val, theArr.size());
        theArr.add(val);
        return true;
    }

    public boolean remove(int val) {
        if(!theMap.containsKey(val)){
            return false;
        }
        int lastIndex = theArr.size()-1;
        int temp = theArr.get(lastIndex);
        int indexToRemove = theMap.get(val);

        theArr.set(indexToRemove, temp);
        theArr.remove(lastIndex);
        theMap.put(temp, indexToRemove);
        theMap.remove(val);
        return true;
    }

    public int getRandom() {
        Random r= new Random();
        int indexToReturn = r.nextInt(theArr.size());
        return theArr.get(indexToReturn);
    }
}
