import java.io.FileReader;
import java.io.FileWriter;

import java.util.List;
import java.util.ArrayList;

import org.topcoder.TopcoderReader;
import org.topcoder.TopcoderWriter;
import org.topcoder.TypeRef;

public class ATaleOfThreeCitiesSolver {
    public static void main(String[] args) {
    try {
        TopcoderReader reader = new TopcoderReader(new FileReader(args[0]));
        List<Integer> axBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] ax = new int[axBoxed.size()];
        for (int _i = 0; _i < axBoxed.size(); ++_i)
            ax[_i] = axBoxed.get(_i);
        reader.next();
        
        List<Integer> ayBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] ay = new int[ayBoxed.size()];
        for (int _i = 0; _i < ayBoxed.size(); ++_i)
            ay[_i] = ayBoxed.get(_i);
        reader.next();
        
        List<Integer> bxBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] bx = new int[bxBoxed.size()];
        for (int _i = 0; _i < bxBoxed.size(); ++_i)
            bx[_i] = bxBoxed.get(_i);
        reader.next();
        
        List<Integer> byBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] by = new int[byBoxed.size()];
        for (int _i = 0; _i < byBoxed.size(); ++_i)
            by[_i] = byBoxed.get(_i);
        reader.next();
        
        List<Integer> cxBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] cx = new int[cxBoxed.size()];
        for (int _i = 0; _i < cxBoxed.size(); ++_i)
            cx[_i] = cxBoxed.get(_i);
        reader.next();
        
        List<Integer> cyBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] cy = new int[cyBoxed.size()];
        for (int _i = 0; _i < cyBoxed.size(); ++_i)
            cy[_i] = cyBoxed.get(_i);
        reader.close();

        ATaleOfThreeCities solver = new ATaleOfThreeCities();
        TopcoderWriter writer = new TopcoderWriter(new FileWriter(args[1]));
        writer.write(solver.connect(ax, ay, bx, by, cx, cy));
        writer.close();
    } catch (Exception err) {
        err.printStackTrace(System.err);
    }
    }
}
