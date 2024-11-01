; ModuleID = 'tests/multiplication.c'
source_filename = "tests/multiplication.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

; Function Attrs: noinline nounwind optnone ssp uwtable(sync)
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca float, align 4
  %3 = alloca float, align 4
  %4 = alloca float, align 4
  %5 = alloca float, align 4
  %6 = alloca float, align 4
  %7 = alloca float, align 4
  %8 = alloca float, align 4
  %9 = alloca float, align 4
  %10 = alloca float, align 4
  %11 = alloca float, align 4
  %12 = alloca float, align 4
  %13 = alloca float, align 4
  %14 = alloca float, align 4
  %15 = alloca float, align 4
  %16 = alloca float, align 4
  %17 = alloca float, align 4
  %18 = alloca float, align 4
  %19 = alloca float, align 4
  %20 = alloca float, align 4
  %21 = alloca float, align 4
  store i32 0, ptr %1, align 4
  store float 0x3FF19999A0000000, ptr %2, align 4
  store float 0x40019999A0000000, ptr %3, align 4
  store float 0x400A666660000000, ptr %4, align 4
  store float 0x40119999A0000000, ptr %5, align 4
  store float 5.500000e+00, ptr %6, align 4
  store float 0x401A666660000000, ptr %7, align 4
  store float 0x401ECCCCC0000000, ptr %8, align 4
  store float 0x40219999A0000000, ptr %9, align 4
  store float 0x4023CCCCC0000000, ptr %10, align 4
  store float 0x4024333340000000, ptr %11, align 4
  %22 = load float, ptr %2, align 4
  %23 = load float, ptr %3, align 4
  %24 = fmul float %22, %23
  store float %24, ptr %12, align 4
  %25 = load float, ptr %4, align 4
  %26 = load float, ptr %5, align 4
  %27 = fmul float %25, %26
  store float %27, ptr %13, align 4
  %28 = load float, ptr %6, align 4
  %29 = load float, ptr %7, align 4
  %30 = fmul float %28, %29
  store float %30, ptr %14, align 4
  %31 = load float, ptr %8, align 4
  %32 = load float, ptr %9, align 4
  %33 = fmul float %31, %32
  store float %33, ptr %15, align 4
  %34 = load float, ptr %10, align 4
  %35 = load float, ptr %11, align 4
  %36 = fmul float %34, %35
  store float %36, ptr %16, align 4
  %37 = load float, ptr %2, align 4
  %38 = load float, ptr %4, align 4
  %39 = fmul float %37, %38
  store float %39, ptr %17, align 4
  %40 = load float, ptr %6, align 4
  %41 = load float, ptr %8, align 4
  %42 = fmul float %40, %41
  store float %42, ptr %18, align 4
  %43 = load float, ptr %10, align 4
  %44 = load float, ptr %2, align 4
  %45 = fmul float %43, %44
  store float %45, ptr %19, align 4
  %46 = load float, ptr %3, align 4
  %47 = load float, ptr %7, align 4
  %48 = fmul float %46, %47
  store float %48, ptr %20, align 4
  %49 = load float, ptr %5, align 4
  %50 = load float, ptr %9, align 4
  %51 = fmul float %49, %50
  store float %51, ptr %21, align 4
  ret i32 0
}

attributes #0 = { noinline nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+complxnum,+crc,+dotprod,+fp-armv8,+fp16fml,+fullfp16,+jsconv,+lse,+neon,+pauth,+ras,+rcpc,+rdm,+sha2,+sha3,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"uwtable", i32 1}
!3 = !{i32 7, !"frame-pointer", i32 1}
!4 = !{!"Homebrew clang version 18.1.8"}
