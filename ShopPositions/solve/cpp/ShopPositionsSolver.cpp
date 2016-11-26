#include <fstream>
#include <topcoder>
#include "ShopPositions.cpp"
namespace tc = TopCoder;

int main(int argc, char const *argv[]) {
  try {
    std::ifstream ifs(argv[1]);
    int n; tc::read(ifs, n); tc::next(ifs);
    int m; tc::read(ifs, m); tc::next(ifs);
    vector<int> c; tc::read(ifs, c);
    ifs.close();

    std::ofstream ofs(argv[2]);
    ShopPositions solver;
    tc::show(ofs, solver.maxProfit(n, m, c));
    ofs.close();
  } catch (std::exception &e) {
    std::cerr << e.what() << std::endl;
  }
  return 0;
}
