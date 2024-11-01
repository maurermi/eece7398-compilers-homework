; ModuleID = 'tests/nested-conditionals.c'
source_filename = "tests/nested-conditionals.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@.str = private unnamed_addr constant [18 x i8] c"Final result: %f\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable(sync)
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca float, align 4
  %3 = alloca float, align 4
  %4 = alloca float, align 4
  store i32 0, ptr %1, align 4
  store float 0x400D9999A0000000, ptr %2, align 4
  store float 2.500000e+00, ptr %3, align 4
  store float 0.000000e+00, ptr %4, align 4
  %5 = load float, ptr %2, align 4
  %6 = load float, ptr %3, align 4
  %7 = fcmp ogt float %5, %6
  br i1 %7, label %8, label %17

8:                                                ; preds = %0
  %9 = load float, ptr %2, align 4
  %10 = fpext float %9 to double
  %11 = call double @llvm.pow.f64(double %10, double 2.000000e+00)
  %12 = load float, ptr %3, align 4
  %13 = fpext float %12 to double
  %14 = call double @llvm.sqrt.f64(double %13)
  %15 = fsub double %11, %14
  %16 = fptrunc double %15 to float
  store float %16, ptr %4, align 4
  br label %28

17:                                               ; preds = %0
  %18 = load float, ptr %2, align 4
  %19 = load float, ptr %3, align 4
  %20 = fadd float %18, %19
  %21 = fpext float %20 to double
  %22 = call double @llvm.log.f64(double %21)
  %23 = load float, ptr %2, align 4
  %24 = fpext float %23 to double
  %25 = call double @llvm.sin.f64(double %24)
  %26 = fmul double %22, %25
  %27 = fptrunc double %26 to float
  store float %27, ptr %4, align 4
  br label %28

28:                                               ; preds = %17, %8
  %29 = load float, ptr %4, align 4
  %30 = fpext float %29 to double
  %31 = fcmp ogt double %30, 5.000000e+00
  br i1 %31, label %32, label %37

32:                                               ; preds = %28
  %33 = load float, ptr %4, align 4
  %34 = fpext float %33 to double
  %35 = fdiv double %34, 2.000000e+00
  %36 = fptrunc double %35 to float
  store float %36, ptr %4, align 4
  br label %52

37:                                               ; preds = %28
  %38 = load float, ptr %4, align 4
  %39 = fpext float %38 to double
  %40 = fcmp olt double %39, -5.000000e+00
  br i1 %40, label %41, label %46

41:                                               ; preds = %37
  %42 = load float, ptr %4, align 4
  %43 = fpext float %42 to double
  %44 = fmul double %43, -1.000000e+00
  %45 = fptrunc double %44 to float
  store float %45, ptr %4, align 4
  br label %51

46:                                               ; preds = %37
  %47 = load float, ptr %4, align 4
  %48 = fpext float %47 to double
  %49 = fadd double %48, 1.500000e+00
  %50 = fptrunc double %49 to float
  store float %50, ptr %4, align 4
  br label %51

51:                                               ; preds = %46, %41
  br label %52

52:                                               ; preds = %51, %32
  %53 = load float, ptr %4, align 4
  %54 = fpext float %53 to double
  %55 = call i32 (ptr, ...) @printf(ptr noundef @.str, double noundef %54)
  ret i32 0
}

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.pow.f64(double, double) #1

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.sqrt.f64(double) #1

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.log.f64(double) #1

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.sin.f64(double) #1

declare i32 @printf(ptr noundef, ...) #2

attributes #0 = { noinline nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+complxnum,+crc,+dotprod,+fp-armv8,+fp16fml,+fullfp16,+jsconv,+lse,+neon,+pauth,+ras,+rcpc,+rdm,+sha2,+sha3,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #1 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }
attributes #2 = { "frame-pointer"="non-leaf" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+complxnum,+crc,+dotprod,+fp-armv8,+fp16fml,+fullfp16,+jsconv,+lse,+neon,+pauth,+ras,+rcpc,+rdm,+sha2,+sha3,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"uwtable", i32 1}
!3 = !{i32 7, !"frame-pointer", i32 1}
!4 = !{!"Homebrew clang version 18.1.8"}
