import java.io.FileReader;
import java.io.FileWriter;

import java.util.List;
import java.util.ArrayList;

import org.topcoder.TopcoderReader;
import org.topcoder.TopcoderWriter;
import org.topcoder.TypeRef;

public class SwappingParenthesesSolver {
    public static void main(String[] args) {
    try {
        TopcoderReader reader = new TopcoderReader(new FileReader(args[0]));
        String s = (String) reader.next(String.class);
        reader.next();
        
        List<Integer> opBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] op = new int[opBoxed.size()];
        for (int _i = 0; _i < opBoxed.size(); ++_i)
            op[_i] = opBoxed.get(_i);
        reader.close();

        SwappingParentheses solver = new SwappingParentheses();
        TopcoderWriter writer = new TopcoderWriter(new FileWriter(args[1]));
        writer.write(solver.countValid(s, op));
        writer.close();
    } catch (Exception err) {
        err.printStackTrace(System.err);
    }
    }
}
