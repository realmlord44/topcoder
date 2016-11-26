#include <fstream>
#include <topcoder>
#include "ATaleOfThreeCities.cpp"
namespace tc = TopCoder;

int main(int argc, char const *argv[]) {
  try {
    std::ifstream ifs(argv[1]);
    vector<int> ax; tc::read(ifs, ax); tc::next(ifs);
    vector<int> ay; tc::read(ifs, ay); tc::next(ifs);
    vector<int> bx; tc::read(ifs, bx); tc::next(ifs);
    vector<int> by; tc::read(ifs, by); tc::next(ifs);
    vector<int> cx; tc::read(ifs, cx); tc::next(ifs);
    vector<int> cy; tc::read(ifs, cy);
    ifs.close();

    std::ofstream ofs(argv[2]);
    ATaleOfThreeCities solver;
    tc::show(ofs, solver.connect(ax, ay, bx, by, cx, cy));
    ofs.close();
  } catch (std::exception &e) {
    std::cerr << e.what() << std::endl;
  }
  return 0;
}
