.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static factorial(I)I

    iload 0    ; delta = 1
    ldc 1    ; delta = 1
    if_icmpgt NOT_IF_0    ; delta = -2
    ldc 1    ; delta = 1
    ireturn    ; delta = -1
NOT_IF_0:
    iload 0    ; delta = 1
    iload 0    ; delta = 1
    ldc 1    ; delta = 1
    isub    ; delta = -1
    invokestatic Test/factorial(I)I    ; delta = 0
    imul    ; delta = -1
    ireturn    ; delta = -1
    return
.limit locals 1
.limit stack 3
.end method
.method public static main([Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta = 1
    ldc 5    ; delta = 1
    invokestatic Test/factorial(I)I    ; delta = 0
    invokevirtual java/io/PrintStream/print(I)V
    ; delta = -2
    getstatic java/lang/System/out Ljava/io/PrintStream;    ; delta = 1
    invokevirtual java/io/PrintStream/println()V
    ; delta = -1
    return
.limit stack 2
.end method
