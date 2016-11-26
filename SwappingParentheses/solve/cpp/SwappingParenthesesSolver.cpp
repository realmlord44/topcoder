#include <fstream>
#include <topcoder>
#include "SwappingParentheses.cpp"
namespace tc = TopCoder;

int main(int argc, char const *argv[]) {
  try {
    std::ifstream ifs(argv[1]);
    string s; tc::read(ifs, s); tc::next(ifs);
    vector<int> op; tc::read(ifs, op);
    ifs.close();

    std::ofstream ofs(argv[2]);
    SwappingParentheses solver;
    tc::show(ofs, solver.countValid(s, op));
    ofs.close();
  } catch (std::exception &e) {
    std::cerr << e.what() << std::endl;
  }
  return 0;
}
