; ModuleID = 'tests/looping_addition.c'
source_filename = "tests/looping_addition.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@.str = private unnamed_addr constant [15 x i8] c"Final sum: %f\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable(sync)
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca float, align 4
  %3 = alloca float, align 4
  %4 = alloca i32, align 4
  store i32 0, ptr %1, align 4
  store float 1.000000e+00, ptr %2, align 4
  store float 0.000000e+00, ptr %3, align 4
  store i32 0, ptr %4, align 4
  br label %5

5:                                                ; preds = %29, %0
  %6 = load i32, ptr %4, align 4
  %7 = icmp slt i32 %6, 5
  br i1 %7, label %8, label %32

8:                                                ; preds = %5
  %9 = load float, ptr %2, align 4
  %10 = load i32, ptr %4, align 4
  %11 = add nsw i32 %10, 1
  %12 = sitofp i32 %11 to float
  %13 = fdiv float %9, %12
  %14 = load float, ptr %3, align 4
  %15 = fadd float %14, %13
  store float %15, ptr %3, align 4
  %16 = load float, ptr %3, align 4
  %17 = fpext float %16 to double
  %18 = fcmp ogt double %17, 2.000000e+00
  br i1 %18, label %19, label %24

19:                                               ; preds = %8
  %20 = load float, ptr %3, align 4
  %21 = fpext float %20 to double
  %22 = fmul double %21, 5.000000e-01
  %23 = fptrunc double %22 to float
  store float %23, ptr %3, align 4
  br label %24

24:                                               ; preds = %19, %8
  %25 = load float, ptr %2, align 4
  %26 = fpext float %25 to double
  %27 = fadd double %26, 1.000000e+00
  %28 = fptrunc double %27 to float
  store float %28, ptr %2, align 4
  br label %29

29:                                               ; preds = %24
  %30 = load i32, ptr %4, align 4
  %31 = add nsw i32 %30, 1
  store i32 %31, ptr %4, align 4
  br label %5, !llvm.loop !5

32:                                               ; preds = %5
  %33 = load float, ptr %3, align 4
  %34 = fpext float %33 to double
  %35 = call i32 (ptr, ...) @printf(ptr noundef @.str, double noundef %34)
  ret i32 0
}

declare i32 @printf(ptr noundef, ...) #1

attributes #0 = { noinline nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+complxnum,+crc,+dotprod,+fp-armv8,+fp16fml,+fullfp16,+jsconv,+lse,+neon,+pauth,+ras,+rcpc,+rdm,+sha2,+sha3,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #1 = { "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+complxnum,+crc,+dotprod,+fp-armv8,+fp16fml,+fullfp16,+jsconv,+lse,+neon,+pauth,+ras,+rcpc,+rdm,+sha2,+sha3,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"uwtable", i32 1}
!3 = !{i32 7, !"frame-pointer", i32 1}
!4 = !{!"Homebrew clang version 18.1.8"}
!5 = distinct !{!5, !6}
!6 = !{!"llvm.loop.mustprogress"}
