# Undocumented functions - Names derived from debug symbols
1  stdcall -noname QueryThemeServices()
2  stdcall -noname OpenThemeFile(wstr wstr ptr ptr long)
3  stdcall -noname CloseThemeFile(ptr)
4  stdcall -noname ApplyTheme(ptr long ptr)
7  stdcall -noname GetThemeDefaults(wstr wstr long wstr long)
8  stdcall -noname EnumThemes(wstr ptr ptr)
9  stdcall -noname EnumThemeColors(wstr wstr long wstr)
10 stdcall -noname EnumThemeSizes(wstr wstr long ptr)
11 stdcall -noname ParseThemeIniFile(wstr wstr ptr ptr)
13 stdcall -noname DrawNCPreview(ptr long ptr wstr wstr wstr ptr ptr)
14 stdcall -noname RegisterDefaultTheme(wstr long)
15 stdcall -noname DumpLoadedThemeToTextFile(ptr wstr long long)
16 stdcall -noname OpenThemeDataFromFile(ptr ptr wstr long)
17 stdcall -noname OpenThemeFileFromData(ptr ptr)
18 stdcall -noname GetThemeSysSize96(long long)
19 stdcall -noname GetThemeSysFont96(long long ptr)
20 stdcall -noname SessionAllocate(ptr ptr ptr ptr ptr ptr ptr)
21 stdcall -noname SessionFree(ptr)
22 stdcall -noname ThemeHooksOn(ptr)
23 stdcall -noname ThemeHooksOff(ptr)
24 stdcall -noname AreThemeHooksActive(ptr)
25 stdcall -noname GetCurrentChangeNumber(ptr)
26 stdcall -noname GetNewChangeNumber(ptr)
27 stdcall -noname SetGlobalTheme(ptr ptr)
28 stdcall -noname GetGlobalTheme(ptr ptr)
29 stdcall -noname CheckThemeSignature(wstr)
30 stdcall -noname LoadTheme(long long long wstr long long long)
31 stdcall -noname InitUserTheme(ptr)
32 stdcall -noname InitUserRegistry()
33 stdcall -noname ReestablishServerConnection()
34 stdcall -noname ThemeHooksInstall()
35 stdcall -noname ThemeHooksRemove()
36 stdcall -noname RefreshThemeForTS()
43 stdcall -noname ClassicGetSystemMetrics(long)
44 stdcall -noname ClassicSystemParametersInfoA(long long ptr long)
45 stdcall -noname ClassicSystemParametersInfoW(long long ptr long)
46 stdcall -noname ClassicAdjustWindowRectEx(ptr long long long)
48 stdcall -noname GetThemeParseErrorInfo(ptr)
60 stdcall -noname CreateThemeDataFromObjects(ptr ptr long)
61 stdcall -noname OpenThemeDataEx(ptr wstr long)
62 stdcall -noname ServerClearStockObjects(ptr)
63 stdcall -noname MarkSection(ptr long long)
64 stdcall -noname ProcessLoadTheme_RunDLLW(long long ptr long)
65 stdcall -noname SetSystemVisualStyle(wstr long long ptr)
66 stdcall -noname ServiceClearStockObjects(long ptr)
73 stdcall -noname IsThemeActiveByPolicy()


# Standard functions
5 stdcall CloseThemeData(ptr)
6 stdcall DrawThemeBackground(ptr ptr long long ptr ptr)
47 stdcall DrawThemeBackgroundEx(ptr ptr long long ptr ptr)
12 stdcall DrawThemeEdge(ptr ptr long long ptr long long ptr)
37 stdcall DrawThemeIcon(ptr ptr long long ptr ptr long)
38 stdcall DrawThemeParentBackground(ptr ptr ptr)
39 stdcall DrawThemeText(ptr ptr long long wstr long long long ptr)
40 stdcall EnableThemeDialogTexture(ptr long)
41 stdcall EnableTheming(long)
42 stdcall GetCurrentThemeName(wstr long wstr long wstr long)
49 stdcall GetThemeAppProperties()
50 stdcall GetThemeBackgroundContentRect(ptr ptr long long ptr ptr)
51 stdcall GetThemeBackgroundExtent(ptr ptr long long ptr ptr)
52 stdcall GetThemeBackgroundRegion(ptr ptr long long ptr ptr)
53 stdcall GetThemeBool(ptr long long long ptr)
54 stdcall GetThemeColor(ptr long long long ptr)
55 stdcall GetThemeDocumentationProperty(wstr wstr wstr long)
56 stdcall GetThemeEnumValue(ptr long long long ptr)
57 stdcall GetThemeFilename(ptr long long long wstr long)
58 stdcall GetThemeFont(ptr ptr long long long ptr)
59 stdcall GetThemeInt(ptr long long long ptr)
67 stdcall GetThemeIntList(ptr long long long ptr)
68 stdcall GetThemeMargins(ptr ptr long long long ptr ptr)
69 stdcall GetThemeMetric(ptr ptr long long long ptr)
70 stdcall GetThemePartSize(ptr ptr long long ptr long ptr)
71 stdcall GetThemePosition(ptr long long long ptr)
72 stdcall GetThemePropertyOrigin(ptr long long long ptr)
74 stdcall GetThemeRect(ptr long long long ptr)
75 stdcall GetThemeString(ptr long long long wstr long)
76 stdcall GetThemeSysBool(ptr long)
77 stdcall GetThemeSysColor(ptr long)
78 stdcall GetThemeSysColorBrush(ptr long)
79 stdcall GetThemeSysFont(ptr long ptr)
80 stdcall GetThemeSysInt(ptr long ptr)
81 stdcall GetThemeSysSize(ptr long)
82 stdcall GetThemeSysString(ptr long wstr long)
83 stdcall GetThemeTextExtent(ptr ptr long long wstr long long ptr ptr)
84 stdcall GetThemeTextMetrics(ptr ptr long long ptr)
85 stdcall GetWindowTheme(ptr)
86 stdcall HitTestThemeBackground(ptr long long long long ptr long double ptr)
87 stdcall IsAppThemed()
88 stdcall IsThemeActive()
89 stdcall IsThemeBackgroundPartiallyTransparent(ptr long long)
90 stdcall IsThemeDialogTextureEnabled(ptr)
91 stdcall IsThemePartDefined(ptr long long)
92 stdcall OpenThemeData(ptr wstr)
93 stdcall SetThemeAppProperties(long)
94 stdcall SetWindowTheme(ptr wstr wstr)
95 stdcall ThemeInitApiHook(long ptr) uxthemebase.ThemeInitApiHook

#From Vista
@ stdcall BeginBufferedAnimation(ptr ptr ptr long ptr ptr ptr ptr)
@ stdcall BeginBufferedPaint(ptr ptr long ptr ptr)
@ stdcall BufferedPaintUnInit()
@ stdcall BufferedPaintInit()
@ stdcall BufferedPaintClear(ptr ptr)
@ stdcall BufferedPaintRenderAnimation(ptr ptr)
@ stdcall BufferedPaintSetAlpha(ptr ptr long)
@ stdcall BufferedPaintStopAllAnimations(ptr)
@ stdcall DrawThemeParentBackgroundEx(ptr ptr long ptr)
@ stdcall DrawThemeTextEx(ptr ptr long long wstr long long ptr ptr)
@ stdcall DrawThemeParentBackgroundEx(ptr ptr long ptr)
@ stdcall EndBufferedAnimation(ptr long)
@ stdcall EndBufferedPaint(ptr long)
@ stdcall FreeThemePropertyValues(ptr)
@ stdcall FreeThemeSymbols(ptr)
@ stdcall GetBufferedPaintBits(ptr ptr ptr)
@ stdcall GetBufferedPaintDC(ptr)
@ stdcall GetBufferedPaintTargetDC(ptr)
@ stdcall GetBufferedPaintTargetRect(ptr ptr)
@ stdcall GetThemeTransitionDuration(ptr long long long long ptr)
@ stdcall GetThemeBitmap(ptr long long long long ptr)
@ stdcall IsCompositionActive()
@ stdcall SetWindowThemeAttribute(long long ptr long)

#From Win7
@ stdcall BeginPanningFeedback(ptr)
@ stdcall EndPanningFeedback(ptr long)
@ stdcall UpdatePanningFeedback(ptr long long long)