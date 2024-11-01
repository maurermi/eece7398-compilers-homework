#include "llvm/Pass.h"
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/raw_ostream.h"

using namespace llvm;

namespace {

// Find all the float operations in a given function
struct FindFloats : public PassInfoMixin<FindFloats> {
  PreservedAnalyses run(Module &M, ModuleAnalysisManager &AM) {
    for (auto &F : M.functions()) {
      for (auto &B : F) {
        for (auto &I : B) {
          if (auto *op = dyn_cast<BinaryOperator>(&I)) {
            IRBuilder<> builder(op);
            switch (op->getOpcode()) {
            case Instruction::FAdd:
              outs() << *op << "\n";
              break;
            case Instruction::FDiv:
              outs() << *op << "\n";
              break;
            case Instruction::FMul:
              outs() << *op << "\n";
              break;
            case Instruction::FSub:
              outs() << *op << "\n";
              break;
            default:
              break;
            }
          }
        }
      }
    }
    return PreservedAnalyses::all();
  };
};
} // namespace

extern "C" LLVM_ATTRIBUTE_WEAK ::llvm::PassPluginLibraryInfo
llvmGetPassPluginInfo() {
  return {.APIVersion = LLVM_PLUGIN_API_VERSION,
          .PluginName = "Find Float Ops",
          .PluginVersion = "v0.1",
          .RegisterPassBuilderCallbacks = [](PassBuilder &PB) {
            PB.registerPipelineStartEPCallback(
                [](ModulePassManager &MPM, OptimizationLevel Level) {
                  MPM.addPass(FindFloats());
                });
          }};
}
