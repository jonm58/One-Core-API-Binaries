1 stdcall ActivateActCtx(ptr ptr)
2 stdcall AddAtomA(str)
3 stdcall AddAtomW(wstr)
4 stdcall AddConsoleAliasA(str str str) ;check
5 stdcall AddConsoleAliasW(wstr wstr wstr) ;check
6 stdcall AddLocalAlternateComputerNameA(str ptr)
7 stdcall AddLocalAlternateComputerNameW(wstr ptr)
8 stdcall AddRefActCtx(ptr)
9 stdcall AddVectoredContinueHandler(long ptr) ntdll.RtlAddVectoredContinueHandler
10 stdcall AddVectoredExceptionHandler(long ptr) ntdll.RtlAddVectoredExceptionHandler
11 stdcall AllocConsole()
12 stdcall AllocateUserPhysicalPages(long ptr ptr)
13 stdcall AreFileApisANSI()
14 stdcall AssignProcessToJobObject(ptr ptr)
15 stdcall AttachConsole(long)
16 stdcall BackupRead(ptr ptr long ptr long long ptr)
17 stdcall BackupSeek(ptr long long ptr ptr ptr)
18 stdcall BackupWrite(ptr ptr long ptr long long ptr)
19 stdcall BaseCheckAppcompatCache(long long long ptr)
20 stdcall BaseCheckRunApp(long ptr long long long long long long long long)
21 stdcall BaseCleanupAppcompatCacheSupport(ptr)
22 stdcall BaseDumpAppcompatCache()
23 stdcall BaseFlushAppcompatCache()
24 stdcall BaseInitAppcompatCacheSupport()
25 stdcall BaseIsAppcompatInfrastructureDisabled() IsShimInfrastructureDisabled
26 stdcall BaseProcessInitPostImport() ; missing in Win 7
;@ stdcall -arch=x86_64 BaseProcessStart()
27 stdcall BaseQueryModuleData(str str ptr ptr ptr) ;check
;@ stdcall -arch=x86_64 BaseThreadStart()
28 stdcall BaseUpdateAppcompatCache(long long long)
29 stdcall BasepCheckBadapp(long ptr long long long long long long long)
30 stdcall BasepCheckWinSaferRestrictions(long long long long long long)
31 stdcall BasepFreeAppCompatData(ptr ptr)
32 stdcall Beep(long long)
33 stdcall BeginUpdateResourceA(str long)
34 stdcall BeginUpdateResourceW(wstr long)
35 stdcall BindIoCompletionCallback(long ptr long)
36 stdcall BuildCommDCBA(str ptr)
37 stdcall BuildCommDCBAndTimeoutsA(str ptr ptr)
38 stdcall BuildCommDCBAndTimeoutsW(wstr ptr ptr)
39 stdcall BuildCommDCBW(wstr ptr)
40 stdcall CallNamedPipeA(str ptr long ptr long ptr long)
41 stdcall CallNamedPipeW(wstr ptr long ptr long ptr long)
42 stdcall CancelDeviceWakeupRequest(long)
43 stdcall CancelIo(long)
44 stdcall CancelTimerQueueTimer(long long)
45 stdcall CancelWaitableTimer(long)
46 stdcall ChangeTimerQueueTimer(ptr ptr long long)
47 stdcall CheckNameLegalDOS8Dot3A(str str long long long)
48 stdcall CheckNameLegalDOS8Dot3W(wstr str long long long)
49 stdcall CheckRemoteDebuggerPresent(long ptr)
50 stdcall ClearCommBreak(long)
51 stdcall ClearCommError(long ptr ptr)
52 stdcall CloseConsoleHandle(long)
53 stdcall CloseHandle(long)
54 stdcall CloseProfileUserMapping()
55 stdcall CmdBatNotification(long)
56 stdcall CommConfigDialogA(str long ptr)
57 stdcall CommConfigDialogW(wstr long ptr)
58 stdcall CompareFileTime(ptr ptr)
59 stdcall CompareStringA(long long str long str long)
60 stdcall CompareStringW(long long wstr long wstr long)
61 stdcall ConnectNamedPipe(long ptr)
;@ stdcall -arch=x86_64 ConsoleIMERoutine()
62 stdcall ConsoleMenuControl(long long long)
63 stdcall ContinueDebugEvent(long long long)
64 stdcall ConvertDefaultLocale (long)
65 stdcall ConvertFiberToThread()
66 stdcall ConvertThreadToFiber(ptr)
67 stdcall ConvertThreadToFiberEx(ptr long)
68 stdcall CopyFileA(str str long)
69 stdcall CopyFileExA (str str ptr ptr ptr long)
70 stdcall CopyFileExW (wstr wstr ptr ptr ptr long)
71 stdcall CopyFileW(wstr wstr long)
72 stdcall CopyLZFile(long long) LZCopy
73 stdcall CreateActCtxA(ptr)
74 stdcall CreateActCtxW(ptr)
75 stdcall CreateConsoleScreenBuffer(long long ptr long ptr)
76 stdcall CreateDirectoryA(str ptr)
77 stdcall CreateDirectoryExA(str str ptr)
78 stdcall CreateDirectoryExW(wstr wstr ptr)
79 stdcall CreateDirectoryW(wstr ptr)
80 stdcall CreateEventA(ptr long long str)
81 stdcall CreateEventW(ptr long long wstr)
82 stdcall CreateFiber(long ptr ptr)
83 stdcall CreateFiberEx(long long long ptr ptr)
84 stdcall CreateFileA(str long long ptr long long long)
85 stdcall CreateFileMappingA(long ptr long long long str)
86 stdcall CreateFileMappingW(long ptr long long long wstr)
87 stdcall CreateFileW(wstr long long ptr long long long)
88 stdcall CreateHardLinkA(str str ptr)
89 stdcall CreateHardLinkW(wstr wstr ptr)
90 stdcall CreateIoCompletionPort(long long long long)
91 stdcall CreateJobObjectA(ptr str)
92 stdcall CreateJobObjectW(ptr wstr)
93 stdcall CreateJobSet(long ptr long)
94 stdcall CreateMailslotA(ptr long long ptr)
95 stdcall CreateMailslotW(ptr long long ptr)
96 stdcall CreateMemoryResourceNotification(long)
97 stdcall CreateMutexA(ptr long str)
98 stdcall CreateMutexW(ptr long wstr)
99 stdcall CreateNamedPipeA(str long long long long long long ptr)
100 stdcall CreateNamedPipeW(wstr long long long long long long ptr)
101 stdcall CreateNlsSecurityDescriptor(ptr long long) ; missing in Win 7
102 stdcall CreatePipe(ptr ptr ptr long)
103 stdcall CreateProcessA(str str ptr ptr long long ptr str ptr ptr)
104 stdcall CreateProcessInternalA(ptr str str ptr ptr long long ptr str ptr ptr long)
105 stdcall CreateProcessInternalW(ptr wstr wstr ptr ptr long long ptr wstr ptr ptr long)
106 stdcall CreateProcessW(wstr wstr ptr ptr long long ptr wstr ptr ptr)
107 stdcall CreateRemoteThread(long ptr long ptr long long ptr)
108 stdcall CreateSemaphoreA(ptr long long str)
109 stdcall CreateSemaphoreW(ptr long long wstr)
110 stdcall -i386 CreateSocketHandle()
111 stdcall CreateTapePartition(long long long long)
112 stdcall CreateThread(ptr long ptr long long ptr)
113 stdcall CreateTimerQueue ()
114 stdcall CreateTimerQueueTimer(ptr long ptr ptr long long long)
115 stdcall CreateToolhelp32Snapshot(long long)
116 stdcall CreateWaitableTimerA(ptr long str)
117 stdcall CreateWaitableTimerW(ptr long wstr)
;@ stdcall -arch=x86_64 CtrlRoutine()
118 stdcall DeactivateActCtx(long ptr)
119 stdcall DebugActiveProcess(long)
120 stdcall DebugActiveProcessStop(long)
121 stdcall DebugBreak() ntdll.DbgBreakPoint
122 stdcall DebugBreakProcess(long)
123 stdcall DebugSetProcessKillOnExit(long)
124 stdcall DecodePointer(ptr) ntdll.RtlDecodePointer
125 stdcall DecodeSystemPointer(ptr) ntdll.RtlDecodeSystemPointer
126 stdcall DefineDosDeviceA(long str str)
127 stdcall DefineDosDeviceW(long wstr wstr)
128 stdcall DelayLoadFailureHook(str str)
129 stdcall DeleteAtom(long)
130 stdcall DeleteCriticalSection(ptr) ntdll.RtlDeleteCriticalSection
131 stdcall DeleteFiber(ptr)
132 stdcall DeleteFileA(str)
133 stdcall DeleteFileW(wstr)
134 stdcall DeleteTimerQueue(long)
135 stdcall DeleteTimerQueueEx (long long)
136 stdcall DeleteTimerQueueTimer(long long long)
137 stdcall DeleteVolumeMountPointA(str) ;check
138 stdcall DeleteVolumeMountPointW(wstr) ;check
139 stdcall DeviceIoControl(long long ptr long ptr long ptr ptr)
140 stdcall DisableThreadLibraryCalls(long)
141 stdcall DisconnectNamedPipe(long)
142 stdcall DnsHostnameToComputerNameA (str ptr ptr)
143 stdcall DnsHostnameToComputerNameW (wstr ptr ptr)
144 stdcall DosDateTimeToFileTime(long long ptr)
145 stdcall DosPathToSessionPathA(long str str)
146 stdcall DosPathToSessionPathW(long wstr wstr)
147 stdcall DuplicateConsoleHandle(long long long long)
148 stdcall DuplicateHandle(long long long ptr long long long)
149 stdcall EncodePointer(ptr) ntdll.RtlEncodePointer
150 stdcall EncodeSystemPointer(ptr) ntdll.RtlEncodeSystemPointer
151 stdcall EndUpdateResourceA(long long)
152 stdcall EndUpdateResourceW(long long)
153 stdcall EnterCriticalSection(ptr) ntdll.RtlEnterCriticalSection
154 stdcall EnumCalendarInfoA(ptr long long long)
155 stdcall EnumCalendarInfoExA(ptr long long long)
156 stdcall EnumCalendarInfoExW(ptr long long long)
157 stdcall EnumCalendarInfoW(ptr long long long)
158 stdcall EnumDateFormatsA(ptr long long)
159 stdcall EnumDateFormatsExA(ptr long long)
160 stdcall EnumDateFormatsExW(ptr long long)
161 stdcall EnumDateFormatsW(ptr long long)
162 stdcall EnumLanguageGroupLocalesA(ptr long long ptr)
163 stdcall EnumLanguageGroupLocalesW(ptr long long ptr)
164 stdcall EnumResourceLanguagesA(long str str ptr long)
165 stdcall EnumResourceLanguagesW(long wstr wstr ptr long)
166 stdcall EnumResourceNamesA(long str ptr long)
167 stdcall EnumResourceNamesW(long wstr ptr long)
168 stdcall EnumResourceTypesA(long ptr long)
169 stdcall EnumResourceTypesW(long ptr long)
170 stdcall EnumSystemCodePagesA(ptr long)
171 stdcall EnumSystemCodePagesW(ptr long)
172 stdcall EnumSystemFirmwareTables(long ptr long)
173 stdcall EnumSystemGeoID(long long ptr)
174 stdcall EnumSystemLanguageGroupsA(ptr long ptr)
175 stdcall EnumSystemLanguageGroupsW(ptr long ptr)
176 stdcall EnumSystemLocalesA(ptr long)
177 stdcall EnumSystemLocalesW(ptr long)
178 stdcall EnumTimeFormatsA(ptr long long)
179 stdcall EnumTimeFormatsW(ptr long long)
180 stdcall EnumUILanguagesA(ptr long long)
181 stdcall EnumUILanguagesW(ptr long long)
182 stdcall EnumerateLocalComputerNamesA(ptr long str ptr)
183 stdcall EnumerateLocalComputerNamesW(ptr long wstr ptr)
184 stdcall EraseTape(ptr long long)
185 stdcall EscapeCommFunction(long long)
186 stdcall ExitProcess(long) ; FIXME: ntdll.RtlExitUserProcess
187 stdcall ExitThread(long) ; FIXME: ntdll.RtlExitUserThread
188 stdcall ExitVDM(long long)
189 stdcall ExpandEnvironmentStringsA(str ptr long)
190 stdcall ExpandEnvironmentStringsW(wstr ptr long)
191 stdcall ExpungeConsoleCommandHistoryA(long)
192 stdcall ExpungeConsoleCommandHistoryW(long)
193 stdcall FatalAppExitA(long str)
194 stdcall FatalAppExitW(long wstr)
195 stdcall FatalExit(long)
196 stdcall FileTimeToDosDateTime(ptr ptr ptr)
197 stdcall FileTimeToLocalFileTime(ptr ptr)
198 stdcall FileTimeToSystemTime(ptr ptr)
199 stdcall FillConsoleOutputAttribute(long long long long ptr)
200 stdcall FillConsoleOutputCharacterA(long long long long ptr)
201 stdcall FillConsoleOutputCharacterW(long long long long ptr)
202 stdcall FindActCtxSectionGuid(long ptr long ptr ptr)
203 stdcall FindActCtxSectionStringA(long ptr long str ptr)
204 stdcall FindActCtxSectionStringW(long ptr long wstr ptr)
205 stdcall FindAtomA(str)
206 stdcall FindAtomW(wstr)
207 stdcall FindClose(long)
208 stdcall FindCloseChangeNotification(long)
209 stdcall FindFirstChangeNotificationA(str long long)
210 stdcall FindFirstChangeNotificationW(wstr long long)
211 stdcall FindFirstFileA(str ptr)
212 stdcall FindFirstFileExA(str long ptr long ptr long)
213 stdcall FindFirstFileExW(wstr long ptr long ptr long)
214 stdcall FindFirstFileW(wstr ptr)
215 stdcall FindFirstStreamW(wstr ptr ptr long)
216 stdcall FindFirstVolumeA(ptr long)
217 stdcall FindFirstVolumeMountPointA(str ptr long)
218 stdcall FindFirstVolumeMountPointW(wstr ptr long)
219 stdcall FindFirstVolumeW(ptr long)
220 stdcall FindNextChangeNotification(long)
221 stdcall FindNextFileA(long ptr)
222 stdcall FindNextFileW(long ptr)
223 stdcall FindNextStreamW(ptr ptr)
224 stdcall FindNextVolumeA(long ptr long)
225 stdcall FindNextVolumeMountPointA(long str long)
226 stdcall FindNextVolumeMountPointW(long wstr long)
227 stdcall FindNextVolumeW(long ptr long)
228 stdcall FindResourceA(long str str)
229 stdcall FindResourceExA(long str str long)
230 stdcall FindResourceExW(long wstr wstr long)
231 stdcall FindResourceW(long wstr wstr)
232 stdcall FindVolumeClose(ptr)
233 stdcall FindVolumeMountPointClose(ptr)
234 stdcall FlsAlloc(ptr)
235 stdcall FlsFree(long)
236 stdcall FlsGetValue(long)
237 stdcall FlsSetValue(long ptr)
238 stdcall FlushConsoleInputBuffer(long)
239 stdcall FlushFileBuffers(long)
240 stdcall FlushInstructionCache(long long long)
241 stdcall FlushViewOfFile(ptr long)
242 stdcall FoldStringA(long str long ptr long)
243 stdcall FoldStringW(long wstr long ptr long)
244 stdcall FormatMessageA(long ptr long long ptr long ptr)
245 stdcall FormatMessageW(long ptr long long ptr long ptr)
246 stdcall FreeConsole()
247 stdcall FreeEnvironmentStringsA(ptr)
248 stdcall FreeEnvironmentStringsW(ptr)
249 stdcall FreeLibrary(long)
250 stdcall FreeLibraryAndExitThread(long long)
251 stdcall FreeResource(long)
252 stdcall FreeUserPhysicalPages(long long long)
253 stdcall GenerateConsoleCtrlEvent(long long)
254 stdcall GetACP()
255 stdcall GetAtomNameA(long ptr long)
256 stdcall GetAtomNameW(long ptr long)
257 stdcall GetBinaryType(str ptr) GetBinaryTypeA
258 stdcall GetBinaryTypeA(str ptr)
259 stdcall GetBinaryTypeW(wstr ptr)
260 stdcall GetCPFileNameFromRegistry(long wstr long) ;check missing in Win 7
261 stdcall GetCPInfo(long ptr)
262 stdcall GetCPInfoExA(long long ptr)
263 stdcall GetCPInfoExW(long long ptr)
264 stdcall GetCalendarInfoA(long long long ptr long ptr)
265 stdcall GetCalendarInfoW(long long long ptr long ptr)
266 stdcall GetComPlusPackageInstallStatus()
267 stdcall GetCommConfig(long ptr long)
268 stdcall GetCommMask(long ptr)
269 stdcall GetCommModemStatus(long ptr)
270 stdcall GetCommProperties(long ptr)
271 stdcall GetCommState(long ptr)
272 stdcall GetCommTimeouts(long ptr)
273 stdcall GetCommandLineA()
274 stdcall GetCommandLineW()
275 stdcall GetCompressedFileSizeA(long ptr)
276 stdcall GetCompressedFileSizeW(long ptr)
277 stdcall GetComputerNameA(ptr ptr)
278 stdcall GetComputerNameExA(long ptr ptr)
279 stdcall GetComputerNameExW(long ptr ptr)
280 stdcall GetComputerNameW(ptr ptr)
281 stdcall GetConsoleAliasA(str str long str)
282 stdcall GetConsoleAliasExesA(str long)
283 stdcall GetConsoleAliasExesLengthA()
284 stdcall GetConsoleAliasExesLengthW()
285 stdcall GetConsoleAliasExesW(wstr long)
286 stdcall GetConsoleAliasW(wstr ptr long wstr)
287 stdcall GetConsoleAliasesA(str long str)
288 stdcall GetConsoleAliasesLengthA(str)
289 stdcall GetConsoleAliasesLengthW(wstr)
290 stdcall GetConsoleAliasesW(wstr long wstr)
291 stdcall GetConsoleCP()
292 stdcall GetConsoleCharType(long long ptr)
293 stdcall GetConsoleCommandHistoryA(long long long)
294 stdcall GetConsoleCommandHistoryLengthA(long)
295 stdcall GetConsoleCommandHistoryLengthW(long)
296 stdcall GetConsoleCommandHistoryW(long long long)
297 stdcall GetConsoleCursorInfo(long ptr)
298 stdcall GetConsoleCursorMode(long ptr ptr)
299 stdcall GetConsoleDisplayMode(ptr)
300 stdcall GetConsoleFontInfo(long long long ptr)
301 stdcall GetConsoleFontSize(long long)
302 stdcall GetConsoleHardwareState(long long ptr)
303 stdcall GetConsoleInputExeNameA(long ptr)
304 stdcall GetConsoleInputExeNameW(long ptr)
305 stdcall GetConsoleInputWaitHandle()
306 stdcall GetConsoleKeyboardLayoutNameA(ptr)
307 stdcall GetConsoleKeyboardLayoutNameW(ptr)
308 stdcall GetConsoleMode(long ptr)
309 stdcall GetConsoleNlsMode(long ptr)
310 stdcall GetConsoleOutputCP()
311 stdcall GetConsoleProcessList(ptr long) ; missing in XP SP3
312 stdcall GetConsoleScreenBufferInfo(long ptr)
313 stdcall GetConsoleSelectionInfo(ptr)
314 stdcall GetConsoleTitleA(ptr long)
315 stdcall GetConsoleTitleW(ptr long)
316 stdcall GetConsoleWindow()
317 stdcall GetCurrencyFormatA(long long str ptr str long)
318 stdcall GetCurrencyFormatW(long long str ptr str long)
319 stdcall GetCurrentActCtx(ptr)
320 stdcall GetCurrentConsoleFont(long long ptr)
321 stdcall GetCurrentDirectoryA(long ptr)
322 stdcall GetCurrentDirectoryW(long ptr)
323 stdcall -norelay GetCurrentProcess()
324 stdcall -norelay GetCurrentProcessId()
325 stdcall GetCurrentProcessorNumber() ntdll.RtlGetCurrentProcessorNumber
326 stdcall -norelay GetCurrentThread()
327 stdcall -norelay GetCurrentThreadId()
328 stdcall GetDateFormatA(long long ptr str ptr long)
329 stdcall GetDateFormatW(long long ptr wstr ptr long)
330 stdcall GetDefaultCommConfigA(str ptr long)
331 stdcall GetDefaultCommConfigW(wstr ptr long)
332 stdcall GetDefaultSortkeySize(ptr) ; missing in Win 7
333 stdcall GetDevicePowerState(long ptr)
334 stdcall GetDiskFreeSpaceA(str ptr ptr ptr ptr)
335 stdcall GetDiskFreeSpaceExA (str ptr ptr ptr)
336 stdcall GetDiskFreeSpaceExW (wstr ptr ptr ptr)
337 stdcall GetDiskFreeSpaceW(wstr ptr ptr ptr ptr)
338 stdcall GetDllDirectoryA(long ptr)
339 stdcall GetDllDirectoryW(long ptr)
340 stdcall GetDriveTypeA(str)
341 stdcall GetDriveTypeW(wstr)
342 stdcall GetEnvironmentStrings()
343 stdcall GetEnvironmentStringsA() GetEnvironmentStrings
344 stdcall GetEnvironmentStringsW()
345 stdcall GetEnvironmentVariableA(str ptr long)
346 stdcall GetEnvironmentVariableW(wstr ptr long)
347 stdcall GetExitCodeProcess(long ptr)
348 stdcall GetExitCodeThread(long ptr)
349 stdcall GetExpandedNameA(str ptr)
350 stdcall GetExpandedNameW(wstr ptr)
351 stdcall GetFileAttributesA(str)
352 stdcall GetFileAttributesExA(str long ptr)
353 stdcall GetFileAttributesExW(wstr long ptr)
354 stdcall GetFileAttributesW(wstr)
355 stdcall GetFileInformationByHandle(long ptr)
356 stdcall GetFileSize(long ptr)
357 stdcall GetFileSizeEx(long ptr)
358 stdcall GetFileTime(long ptr ptr ptr)
359 stdcall GetFileType(long)
360 stdcall GetFirmwareEnvironmentVariableA(str str ptr long)
361 stdcall GetFirmwareEnvironmentVariableW(wstr wstr ptr long)
362 stdcall GetFullPathNameA(str long ptr ptr)
363 stdcall GetFullPathNameW(wstr long ptr ptr)
364 stdcall GetGeoInfoA(long long ptr long long)
365 stdcall GetGeoInfoW(long long ptr long long)
366 stdcall -i386 GetHandleContext(long) ; missing on x64
367 stdcall GetHandleInformation(long ptr)
368 stdcall GetLargePageMinimum()
369 stdcall GetLargestConsoleWindowSize(long)
370 stdcall GetLastError() ntdll.RtlGetLastWin32Error
371 stdcall GetLinguistLangSize(ptr) ; missing in Win 7
372 stdcall GetLocalTime(ptr)
373 stdcall GetLocaleInfoA(long long ptr long)
374 stdcall GetLocaleInfoW(long long ptr long)
375 stdcall GetLogicalDriveStringsA(long ptr)
376 stdcall GetLogicalDriveStringsW(long ptr)
377 stdcall GetLogicalDrives()
378 stdcall GetLogicalProcessorInformation(ptr ptr)
379 stdcall GetLongPathNameA (str long long)
380 stdcall GetLongPathNameW (wstr long long)
381 stdcall GetMailslotInfo(long ptr ptr ptr ptr)
382 stdcall GetModuleFileNameA(long ptr long)
383 stdcall GetModuleFileNameW(long ptr long)
384 stdcall GetModuleHandleA(str)
385 stdcall GetModuleHandleExA(long ptr ptr)
386 stdcall GetModuleHandleExW(long ptr ptr)
387 stdcall GetModuleHandleW(wstr)
388 stdcall GetNLSVersion(long long ptr)
389 stdcall GetNamedPipeHandleStateA(long ptr ptr ptr ptr str long)
390 stdcall GetNamedPipeHandleStateW(long ptr ptr ptr ptr wstr long)
391 stdcall GetNamedPipeInfo(long ptr ptr ptr ptr)
392 stdcall GetNativeSystemInfo(ptr)
393 stdcall GetNextVDMCommand(long)
394 stdcall GetNlsSectionName(long long long str str long) ; missing in Win 7
395 stdcall GetNumaAvailableMemoryNode(long ptr)
396 stdcall GetNumaHighestNodeNumber(ptr)
397 stdcall GetNumaNodeProcessorMask(long ptr)
398 stdcall GetNumaProcessorNode(long ptr)
399 stdcall GetNumberFormatA(long long str ptr ptr long)
400 stdcall GetNumberFormatW(long long wstr ptr ptr long)
401 stdcall GetNumberOfConsoleFonts()
402 stdcall GetNumberOfConsoleInputEvents(long ptr)
403 stdcall GetNumberOfConsoleMouseButtons(ptr)
404 stdcall GetOEMCP()
405 stdcall GetOverlappedResult(long ptr ptr long)
406 stdcall GetPriorityClass(long)
407 stdcall GetPrivateProfileIntA(str str long str)
408 stdcall GetPrivateProfileIntW(wstr wstr long wstr)
409 stdcall GetPrivateProfileSectionA(str ptr long str)
410 stdcall GetPrivateProfileSectionNamesA(ptr long str)
411 stdcall GetPrivateProfileSectionNamesW(ptr long wstr)
412 stdcall GetPrivateProfileSectionW(wstr ptr long wstr)
413 stdcall GetPrivateProfileStringA(str str str ptr long str)
414 stdcall GetPrivateProfileStringW(wstr wstr wstr ptr long wstr)
415 stdcall GetPrivateProfileStructA (str str ptr long str)
416 stdcall GetPrivateProfileStructW(wstr wstr ptr long wstr)
417 stdcall GetProcAddress(long str)
418 stdcall GetProcessAffinityMask(long ptr ptr)
419 stdcall GetProcessHandleCount(long ptr)
420 stdcall -norelay GetProcessHeap()
421 stdcall GetProcessHeaps(long ptr)
422 stdcall GetProcessId(long)
423 stdcall GetProcessIdOfThread(ptr)
424 stdcall GetProcessIoCounters(long ptr)
425 stdcall GetProcessPriorityBoost(long ptr)
426 stdcall GetProcessShutdownParameters(ptr ptr)
427 stdcall GetProcessTimes(long ptr ptr ptr ptr)
428 stdcall GetProcessVersion(long)
429 stdcall GetProcessWorkingSetSize(long ptr ptr)
430 stdcall GetProcessWorkingSetSizeEx(long ptr ptr long)
431 stdcall GetProfileIntA(str str long)
432 stdcall GetProfileIntW(wstr wstr long)
433 stdcall GetProfileSectionA(str ptr long)
434 stdcall GetProfileSectionW(wstr ptr long)
435 stdcall GetProfileStringA(str str str ptr long)
436 stdcall GetProfileStringW(wstr wstr wstr ptr long)
437 stdcall GetQueuedCompletionStatus(long ptr ptr ptr long)
438 stdcall GetShortPathNameA(str ptr long)
439 stdcall GetShortPathNameW(wstr ptr long)
440 stdcall GetStartupInfoA(ptr)
441 stdcall GetStartupInfoW(ptr)
442 stdcall GetStdHandle(long)
443 stdcall GetStringTypeA(long long str long ptr)
444 stdcall GetStringTypeExA(long long str long ptr)
445 stdcall GetStringTypeExW(long long wstr long ptr)
446 stdcall GetStringTypeW(long wstr long ptr)
447 stdcall GetSystemDefaultLCID()
448 stdcall GetSystemDefaultLangID()
449 stdcall GetSystemDefaultUILanguage()
450 stdcall GetSystemDirectoryA(ptr long)
451 stdcall GetSystemDirectoryW(ptr long)
452 stdcall GetSystemFileCacheSize(ptr ptr ptr)
453 stdcall GetSystemFirmwareTable(long long ptr long)
454 stdcall GetSystemInfo(ptr)
455 stdcall GetSystemPowerStatus(ptr)
456 stdcall GetSystemRegistryQuota(ptr ptr)
457 stdcall GetSystemTime(ptr)
458 stdcall GetSystemTimeAdjustment(ptr ptr ptr)
459 stdcall GetSystemTimeAsFileTime(ptr)
460 stdcall GetSystemTimes(ptr ptr ptr)
461 stdcall GetSystemWindowsDirectoryA(ptr long)
462 stdcall GetSystemWindowsDirectoryW(ptr long)
463 stdcall GetSystemWow64DirectoryA(ptr long)
464 stdcall GetSystemWow64DirectoryW(ptr long)
465 stdcall GetTapeParameters(ptr long ptr ptr)
466 stdcall GetTapePosition(ptr long ptr ptr ptr)
467 stdcall GetTapeStatus(ptr)
468 stdcall GetTempFileNameA(str str long ptr)
469 stdcall GetTempFileNameW(wstr wstr long ptr)
470 stdcall GetTempPathA(long ptr)
471 stdcall GetTempPathW(long ptr)
472 stdcall GetThreadContext(long ptr)
473 stdcall GetThreadIOPendingFlag(long ptr)
474 stdcall GetThreadId(ptr)
475 stdcall GetThreadLocale()
476 stdcall GetThreadPriority(long)
477 stdcall GetThreadPriorityBoost(long ptr)
478 stdcall GetThreadSelectorEntry(long long ptr)
479 stdcall GetThreadTimes(long ptr ptr ptr ptr)
480 stdcall GetTickCount()
481 stdcall GetTimeFormatA(long long ptr str ptr long)
482 stdcall GetTimeFormatW(long long ptr wstr ptr long)
483 stdcall GetTimeZoneInformation(ptr)
484 stdcall GetUserDefaultLCID()
485 stdcall GetUserDefaultLangID()
486 stdcall GetUserDefaultUILanguage()
487 stdcall GetUserGeoID(long)
488 stdcall GetVDMCurrentDirectories(long long)
489 stdcall GetVersion()
490 stdcall GetVersionExA(ptr)
491 stdcall GetVersionExW(ptr)
492 stdcall GetVolumeInformationA(str ptr long ptr ptr ptr ptr long)
493 stdcall GetVolumeInformationW(wstr ptr long ptr ptr ptr ptr long)
494 stdcall GetVolumeNameForVolumeMountPointA(str ptr long)
495 stdcall GetVolumeNameForVolumeMountPointW(wstr ptr long)
496 stdcall GetVolumePathNameA(str ptr long)
497 stdcall GetVolumePathNameW(wstr ptr long)
498 stdcall GetVolumePathNamesForVolumeNameA(str str long ptr)
499 stdcall GetVolumePathNamesForVolumeNameW(wstr wstr long ptr)
500 stdcall GetWindowsDirectoryA(ptr long)
501 stdcall GetWindowsDirectoryW(ptr long)
502 stdcall GetWriteWatch(long ptr long ptr ptr ptr)
503 stdcall GlobalAddAtomA(str)
504 stdcall GlobalAddAtomW(wstr)
505 stdcall GlobalAlloc(long long)
506 stdcall GlobalCompact(long)
507 stdcall GlobalDeleteAtom(long)
508 stdcall GlobalFindAtomA(str)
509 stdcall GlobalFindAtomW(wstr)
510 stdcall GlobalFix(long)
511 stdcall GlobalFlags(long)
512 stdcall GlobalFree(long)
513 stdcall GlobalGetAtomNameA(long ptr long)
514 stdcall GlobalGetAtomNameW(long ptr long)
515 stdcall GlobalHandle(ptr)
516 stdcall GlobalLock(long)
517 stdcall GlobalMemoryStatus(ptr)
518 stdcall GlobalMemoryStatusEx(ptr)
519 stdcall GlobalReAlloc(long long long)
520 stdcall GlobalSize(long)
521 stdcall GlobalUnWire(long)
522 stdcall GlobalUnfix(long)
523 stdcall GlobalUnlock(long)
524 stdcall GlobalWire(long)
525 stdcall Heap32First(ptr long long)
526 stdcall Heap32ListFirst(long ptr)
527 stdcall Heap32ListNext(long ptr)
528 stdcall Heap32Next(ptr)
529 stdcall HeapAlloc(long long long) ntdll.RtlAllocateHeap
530 stdcall HeapCompact(long long)
531 stdcall HeapCreate(long long long)
532 stdcall HeapCreateTagsW(long long wstr wstr) ; missing in Win 7
533 stdcall HeapDestroy(long)
534 stdcall HeapExtend(long long ptr long) ; missing in Win 7
535 stdcall HeapFree(long long long) ntdll.RtlFreeHeap
536 stdcall HeapLock(long)
537 stdcall HeapQueryInformation(long long ptr long ptr)
538 stdcall HeapQueryTagW(long long long long ptr) ; missing in Win 7
539 stdcall HeapReAlloc(long long ptr long) ntdll.RtlReAllocateHeap
540 stdcall HeapSetInformation(ptr long ptr long)
541 stdcall HeapSize(long long ptr) ntdll.RtlSizeHeap
542 stdcall HeapSummary(long long ptr)
543 stdcall HeapUnlock(long)
544 stdcall HeapUsage(long long long long ptr) ; missing in Win 7
545 stdcall HeapValidate(long long ptr)
546 stdcall HeapWalk(long ptr)
547 stdcall InitAtomTable(long)
548 stdcall InitializeCriticalSection(ptr)
549 stdcall InitializeCriticalSectionAndSpinCount(ptr long)
550 stdcall InitializeSListHead(ptr) ntdll.RtlInitializeSListHead
551 stdcall -arch=i386 -ret64 InterlockedCompareExchange64(ptr double double) ntdll.RtlInterlockedCompareExchange64
552 stdcall -arch=i386 InterlockedCompareExchange (ptr long long)
553 stdcall -arch=i386 InterlockedDecrement(ptr)
554 stdcall -arch=i386 InterlockedExchange(ptr long)
555 stdcall -arch=i386 InterlockedExchangeAdd(ptr long)
556 stdcall InterlockedFlushSList(ptr) ntdll.RtlInterlockedFlushSList
557 stdcall -arch=i386 InterlockedIncrement(ptr)
558 stdcall InterlockedPopEntrySList(ptr) ntdll.RtlInterlockedPopEntrySList
559 stdcall InterlockedPushEntrySList(ptr ptr) ntdll.RtlInterlockedPushEntrySList
560 stdcall InvalidateConsoleDIBits(long long)
561 stdcall IsBadCodePtr(ptr)
562 stdcall IsBadHugeReadPtr(ptr long)
563 stdcall IsBadHugeWritePtr(ptr long)
564 stdcall IsBadReadPtr(ptr long)
565 stdcall IsBadStringPtrA(ptr long)
566 stdcall IsBadStringPtrW(ptr long)
567 stdcall IsBadWritePtr(ptr long)
568 stdcall IsDBCSLeadByte(long)
569 stdcall IsDBCSLeadByteEx(long long)
570 stdcall IsDebuggerPresent()
571 stdcall IsNLSDefinedString(long long ptr long long)
572 stdcall IsProcessInJob(long long ptr)
573 stdcall IsProcessorFeaturePresent(long)
574 stdcall IsSystemResumeAutomatic()
575 stdcall IsTimeZoneRedirectionEnabled()
576 stdcall IsValidCodePage(long)
577 stdcall IsValidLanguageGroup(long long)
578 stdcall IsValidLocale(long long)
579 stdcall IsValidUILanguage(long) ; missing in Win 7
580 stdcall IsWow64Process(ptr ptr)
581 stdcall LCMapStringA(long long str long ptr long)
582 stdcall LCMapStringW(long long wstr long ptr long)
583 stdcall LZClose(long)
584 stdcall LZCloseFile(long)
585 stdcall LZCopy(long long)
586 stdcall LZCreateFileW(ptr long long long ptr)
587 stdcall LZDone()
588 stdcall LZInit(long)
589 stdcall LZOpenFileA(str ptr long)
590 stdcall LZOpenFileW(wstr ptr long)
591 stdcall LZRead(long str long)
592 stdcall LZSeek(long long long)
593 stdcall LZStart()
594 stdcall LeaveCriticalSection(ptr) ntdll.RtlLeaveCriticalSection
595 stdcall LoadLibraryA(str)
596 stdcall LoadLibraryExA( str long long)
597 stdcall LoadLibraryExW(wstr long long)
598 stdcall LoadLibraryW(wstr)
599 stdcall LoadModule(str ptr)
600 stdcall LoadResource(long long)
601 stdcall LocalAlloc(long long)
602 stdcall LocalCompact(long)
603 stdcall LocalFileTimeToFileTime(ptr ptr)
604 stdcall LocalFlags(long)
605 stdcall LocalFree(long)
606 stdcall LocalHandle(ptr)
607 stdcall LocalLock(long)
608 stdcall LocalReAlloc(long long long)
609 stdcall LocalShrink(long long)
610 stdcall LocalSize(long)
611 stdcall LocalUnlock(long)
612 stdcall LockFile(long long long long long)
613 stdcall LockFileEx(long long long long long ptr)
614 stdcall LockResource(long)
615 stdcall MapUserPhysicalPages(ptr long ptr)
616 stdcall MapUserPhysicalPagesScatter(ptr long ptr)
617 stdcall MapViewOfFile(long long long long long)
618 stdcall MapViewOfFileEx(long long long long long ptr)
619 stdcall Module32First(long ptr)
620 stdcall Module32FirstW(long ptr)
621 stdcall Module32Next(long ptr)
622 stdcall Module32NextW(long ptr)
623 stdcall MoveFileA(str str)
624 stdcall MoveFileExA(str str long)
625 stdcall MoveFileExW(wstr wstr long)
626 stdcall MoveFileW(wstr wstr)
627 stdcall MoveFileWithProgressA(str str ptr ptr long)
628 stdcall MoveFileWithProgressW(wstr wstr ptr ptr long)
629 stdcall MulDiv(long long long)
630 stdcall MultiByteToWideChar(long long str long ptr long)
631 stdcall NeedCurrentDirectoryForExePathA(str)
632 stdcall NeedCurrentDirectoryForExePathW(wstr)
633 stdcall NlsConvertIntegerToString(long long long wstr long) ; missing in Win 7
634 stdcall NlsGetCacheUpdateCount()
635 stdcall NlsResetProcessLocale()
636 stdcall OpenConsoleW(wstr long long long)
637 stdcall OpenDataFile(long long) ; missing in Win 7
638 stdcall OpenEventA(long long str)
639 stdcall OpenEventW(long long wstr)
640 stdcall OpenFile(str ptr long)
641 stdcall OpenFileMappingA(long long str)
642 stdcall OpenFileMappingW(long long wstr)
643 stdcall OpenJobObjectA(long long str)
644 stdcall OpenJobObjectW(long long wstr)
645 stdcall OpenMutexA(long long str)
646 stdcall OpenMutexW(long long wstr)
647 stdcall OpenProcess(long long long)
648 stdcall OpenProfileUserMapping()
649 stdcall OpenSemaphoreA(long long str)
650 stdcall OpenSemaphoreW(long long wstr)
651 stdcall OpenThread(long long long)
652 stdcall OpenWaitableTimerA(long long str)
653 stdcall OpenWaitableTimerW(long long wstr)
654 stdcall OutputDebugStringA(str)
655 stdcall OutputDebugStringW(wstr)
656 stdcall PeekConsoleInputA(ptr ptr long ptr)
657 stdcall PeekConsoleInputW(ptr ptr long ptr)
658 stdcall PeekNamedPipe(long ptr long ptr ptr ptr)
659 stdcall PostQueuedCompletionStatus(long long ptr ptr)
660 stdcall PrepareTape(ptr long long)
661 stdcall PrivCopyFileExW(wstr wstr ptr ptr long long)
662 stdcall PrivMoveFileIdentityW(long long long)
663 stdcall Process32First (ptr ptr)
664 stdcall Process32FirstW (ptr ptr)
665 stdcall Process32Next (ptr ptr)
666 stdcall Process32NextW (ptr ptr)
667 stdcall ProcessIdToSessionId(long ptr)
668 stdcall PulseEvent(long)
669 stdcall PurgeComm(long long)
670 stdcall QueryActCtxW(long ptr ptr long ptr long ptr)
671 stdcall QueryDepthSList(ptr) ntdll.RtlQueryDepthSList
672 stdcall QueryDosDeviceA(str ptr long)
673 stdcall QueryDosDeviceW(wstr ptr long)
674 stdcall QueryInformationJobObject(long long ptr long ptr)
675 stdcall QueryMemoryResourceNotification(ptr ptr)
676 stdcall QueryPerformanceCounter(ptr)
677 stdcall QueryPerformanceFrequency(ptr)
678 stdcall QueueUserAPC(ptr long long)
679 stdcall QueueUserWorkItem(ptr ptr long)
680 stdcall -norelay RaiseException(long long long ptr)
681 stdcall ReOpenFile(ptr long long long)
682 stdcall ReadConsoleA(long ptr long ptr ptr)
683 stdcall ReadConsoleInputA(long ptr long ptr)
684 stdcall ReadConsoleInputExA(long ptr long ptr long)
685 stdcall ReadConsoleInputExW(long ptr long ptr long)
686 stdcall ReadConsoleInputW(long ptr long ptr)
687 stdcall ReadConsoleOutputA(long ptr long long ptr)
688 stdcall ReadConsoleOutputAttribute(long ptr long long ptr)
689 stdcall ReadConsoleOutputCharacterA(long ptr long long ptr)
690 stdcall ReadConsoleOutputCharacterW(long ptr long long ptr)
691 stdcall ReadConsoleOutputW(long ptr long long ptr)
692 stdcall ReadConsoleW(long ptr long ptr ptr)
693 stdcall ReadDirectoryChangesW(long ptr long long long ptr ptr ptr)
694 stdcall ReadFile(long ptr long ptr ptr)
695 stdcall ReadFileEx(long ptr long ptr ptr)
696 stdcall ReadFileScatter(long ptr long ptr ptr)
697 stdcall ReadProcessMemory(long ptr ptr long ptr)
698 stdcall RegisterConsoleIME(ptr ptr)
699 stdcall RegisterConsoleOS2(long)
700 stdcall RegisterConsoleVDM(long long long long long long long long long long long)
701 stdcall RegisterWaitForInputIdle(ptr)
702 stdcall RegisterWaitForSingleObject(ptr long ptr ptr long long)
703 stdcall RegisterWaitForSingleObjectEx(long ptr ptr long long)
704 stdcall RegisterWowBaseHandlers(long)
705 stdcall RegisterWowExec(long)
706 stdcall ReleaseActCtx(ptr)
707 stdcall ReleaseMutex(long)
708 stdcall ReleaseSemaphore(long long ptr)
709 stdcall RemoveDirectoryA(str)
710 stdcall RemoveDirectoryW(wstr)
711 stdcall RemoveLocalAlternateComputerNameA(str long)
712 stdcall RemoveLocalAlternateComputerNameW(wstr long)
713 stdcall RemoveVectoredContinueHandler(ptr) ntdll.RtlRemoveVectoredContinueHandler
714 stdcall RemoveVectoredExceptionHandler(ptr) ntdll.RtlRemoveVectoredExceptionHandler
715 stdcall ReplaceFile(wstr wstr wstr long ptr ptr) ReplaceFileW
716 stdcall ReplaceFileA(str str str long ptr ptr)
717 stdcall ReplaceFileW(wstr wstr wstr long ptr ptr)
718 stdcall RequestDeviceWakeup(long)
719 stdcall RequestWakeupLatency(long)
720 stdcall ResetEvent(long)
721 stdcall ResetWriteWatch(ptr long)
722 stdcall RestoreLastError(long) ntdll.RtlRestoreLastWin32Error
723 stdcall ResumeThread(long)
@ stdcall -arch=x86_64 RtlAddFunctionTable(ptr long long) ntdll.RtlAddFunctionTable
724 stdcall -register RtlCaptureContext(ptr) ntdll.RtlCaptureContext
725 stdcall RtlCaptureStackBackTrace(long long ptr ptr) ntdll.RtlCaptureStackBackTrace
@ stdcall -arch=x86_64 RtlCompareMemory(ptr ptr ptr) ntdll.RtlCompareMemory
@ stdcall -arch=x86_64 RtlCopyMemory(ptr ptr ptr) ntdll.memcpy
@ stdcall -arch=x86_64 RtlDeleteFunctionTable(ptr) ntdll.RtlDeleteFunctionTable
726 stdcall RtlFillMemory(ptr long long) ntdll.RtlFillMemory
@ stdcall -arch=x86_64 RtlInstallFunctionTableCallback(double double long ptr ptr ptr) ntdll.RtlInstallFunctionTableCallback
@ stdcall -arch=x86_64 RtlLookupFunctionEntry(ptr ptr ptr) ntdll.RtlLookupFunctionEntry
727 stdcall RtlMoveMemory(ptr ptr long) ntdll.RtlMoveMemory
@ stdcall -arch=x86_64 RtlPcToFileHeader(ptr ptr) ntdll.RtlPcToFileHeader
@ stdcall -arch=x86_64 RtlRaiseException(ptr) ntdll.RtlRaiseException
@ stdcall -arch=x86_64 RtlRestoreContext(ptr ptr) ntdll.RtlRestoreContext
728 stdcall RtlUnwind(ptr ptr ptr ptr) ntdll.RtlUnwind
@ stdcall -arch=x86_64 RtlUnwindEx(ptr ptr ptr ptr ptr ptr) ntdll.RtlUnwindEx
@ stdcall -arch=x86_64 RtlVirtualUnwind(ptr ptr ptr long) ntdll.RtlVirtualUnwind
729 stdcall RtlZeroMemory(ptr long) ntdll.RtlZeroMemory
730 stdcall ScrollConsoleScreenBufferA(long ptr ptr ptr ptr)
731 stdcall ScrollConsoleScreenBufferW(long ptr ptr ptr ptr)
732 stdcall SearchPathA(str str str long ptr ptr)
733 stdcall SearchPathW(wstr wstr wstr long ptr ptr)
734 stdcall SetCPGlobal(long) ; missing in Win 7
735 stdcall SetCalendarInfoA(long long long str)
736 stdcall SetCalendarInfoW(long long long wstr)
737 stdcall SetClientTimeZoneInformation(ptr)
738 stdcall SetComPlusPackageInstallStatus(ptr)
739 stdcall SetCommBreak(long)
740 stdcall SetCommConfig(long ptr long)
741 stdcall SetCommMask(long ptr)
742 stdcall SetCommState(long ptr)
743 stdcall SetCommTimeouts(long ptr)
744 stdcall SetComputerNameA(str)
745 stdcall SetComputerNameExA(long str)
746 stdcall SetComputerNameExW(long wstr)
747 stdcall SetComputerNameW(wstr)
748 stdcall SetConsoleActiveScreenBuffer(long)
749 stdcall SetConsoleCP(long)
750 stdcall SetConsoleCommandHistoryMode(long) ; missing in win 7
751 stdcall SetConsoleCtrlHandler(ptr long)
752 stdcall SetConsoleCursor(long long)
753 stdcall SetConsoleCursorInfo(long ptr)
754 stdcall SetConsoleCursorMode(long long long)
755 stdcall SetConsoleCursorPosition(long long)
756 stdcall SetConsoleDisplayMode(long long ptr)
757 stdcall SetConsoleFont(long long)
758 stdcall SetConsoleHardwareState(long long long)
759 stdcall SetConsoleIcon(ptr)
760 stdcall SetConsoleInputExeNameA(ptr)
761 stdcall SetConsoleInputExeNameW(ptr)
762 stdcall SetConsoleKeyShortcuts(long long long long)
763 stdcall SetConsoleLocalEUDC(long long long long)
764 stdcall SetConsoleMaximumWindowSize(long long)
765 stdcall SetConsoleMenuClose(long)
766 stdcall SetConsoleMode(long long)
767 stdcall SetConsoleNlsMode(long long)
768 stdcall SetConsoleNumberOfCommandsA(long long)
769 stdcall SetConsoleNumberOfCommandsW(long long)
770 stdcall SetConsoleOS2OemFormat(long)
771 stdcall SetConsoleOutputCP(long)
772 stdcall SetConsolePalette(long long long)
773 stdcall SetConsoleScreenBufferSize(long long)
774 stdcall SetConsoleTextAttribute(long long)
775 stdcall SetConsoleTitleA(str)
776 stdcall SetConsoleTitleW(wstr)
777 stdcall SetConsoleWindowInfo(long long ptr)
778 stdcall SetCriticalSectionSpinCount(ptr long) ntdll.RtlSetCriticalSectionSpinCount
779 stdcall SetCurrentDirectoryA(str)
780 stdcall SetCurrentDirectoryW(wstr)
781 stdcall SetDefaultCommConfigA(str ptr long)
782 stdcall SetDefaultCommConfigW(wstr ptr long)
783 stdcall SetDllDirectoryA(str)
784 stdcall SetDllDirectoryW(wstr)
785 stdcall SetEndOfFile(long)
786 stdcall SetEnvironmentStringsA(ptr)
787 stdcall SetEnvironmentStringsW(ptr)
788 stdcall SetEnvironmentVariableA(str str)
789 stdcall SetEnvironmentVariableW(wstr wstr)
790 stdcall SetErrorMode(long)
791 stdcall SetEvent(long)
792 stdcall SetFileApisToANSI()
793 stdcall SetFileApisToOEM()
794 stdcall SetFileAttributesA(str long)
795 stdcall SetFileAttributesW(wstr long)
796 stdcall SetFileCompletionNotificationModes(ptr long)
797 stdcall SetFilePointer(long long ptr long)
798 stdcall SetFilePointerEx(long double ptr long)
799 stdcall SetFileShortNameA(long str)
800 stdcall SetFileShortNameW(long wstr)
801 stdcall SetFileTime(long ptr ptr ptr)
802 stdcall SetFileValidData(long double)
803 stdcall SetFirmwareEnvironmentVariableA(str str ptr long)
804 stdcall SetFirmwareEnvironmentVariableW(wstr wstr ptr long)
805 stdcall -i386 SetHandleContext(long long) ; missing in Win 7 x64
806 stdcall SetHandleCount(long)
807 stdcall SetHandleInformation(long long long)
808 stdcall SetInformationJobObject(long long ptr long)
809 stdcall SetLastConsoleEventActive() ; missing in XP SP3
810 stdcall SetLastError(long) ntdll.RtlSetLastWin32Error
811 stdcall SetLocalPrimaryComputerNameA(long long) ; missing in XP SP3
812 stdcall SetLocalPrimaryComputerNameW(long long) ; missing in XP SP3
813 stdcall SetLocalTime(ptr)
814 stdcall SetLocaleInfoA(long long str)
815 stdcall SetLocaleInfoW(long long wstr)
816 stdcall SetMailslotInfo(long long)
817 stdcall SetMessageWaitingIndicator(ptr long)
818 stdcall SetNamedPipeHandleState(long ptr ptr ptr)
819 stdcall SetPriorityClass(long long)
820 stdcall SetProcessAffinityMask(long long)
821 stdcall SetProcessPriorityBoost(long long)
822 stdcall SetProcessShutdownParameters(long long)
823 stdcall SetProcessWorkingSetSize(long long long)
824 stdcall SetProcessWorkingSetSizeEx(long long long long)
825 stdcall SetStdHandle(long long)
826 stdcall SetSystemFileCacheSize(long long long)
827 stdcall SetSystemPowerState(long long)
828 stdcall SetSystemTime(ptr)
829 stdcall SetSystemTimeAdjustment(long long)
830 stdcall SetTapeParameters(ptr long ptr)
831 stdcall SetTapePosition(ptr long long long long long)
832 stdcall SetTermsrvAppInstallMode(long)
833 stdcall SetThreadAffinityMask(long long)
834 stdcall SetThreadContext(long ptr)
835 stdcall SetThreadExecutionState(long)
836 stdcall SetThreadIdealProcessor(long long)
837 stdcall SetThreadLocale(long)
838 stdcall SetThreadPriority(long long)
839 stdcall SetThreadPriorityBoost(long long)
840 stdcall SetThreadStackGuarantee(ptr)
841 stdcall SetThreadUILanguage(long)
842 stdcall SetTimeZoneInformation(ptr)
843 stdcall SetTimerQueueTimer(long ptr ptr long long long)
844 stdcall SetUnhandledExceptionFilter(ptr)
845 stdcall SetUserGeoID(long)
846 stdcall SetVDMCurrentDirectories(long long)
847 stdcall SetVolumeLabelA(str str)
848 stdcall SetVolumeLabelW(wstr wstr)
849 stdcall SetVolumeMountPointA(str str)
850 stdcall SetVolumeMountPointW(wstr wstr)
851 stdcall SetWaitableTimer(long ptr long ptr ptr long)
852 stdcall SetupComm(long long long)
853 stdcall ShowConsoleCursor(long long)
854 stdcall SignalObjectAndWait(long long long long)
855 stdcall SizeofResource(long long)
856 stdcall Sleep(long)
857 stdcall SleepEx(long long)
858 stdcall SuspendThread(long)
859 stdcall SwitchToFiber(ptr)
860 stdcall SwitchToThread()
861 stdcall SystemTimeToFileTime(ptr ptr)
862 stdcall SystemTimeToTzSpecificLocalTime (ptr ptr ptr)
863 stdcall TerminateJobObject(long long)
864 stdcall TerminateProcess(long long)
865 stdcall TerminateThread(long long)
866 stdcall TermsrvAppInstallMode()
867 stdcall Thread32First(long ptr)
868 stdcall Thread32Next(long ptr)
869 stdcall TlsAlloc()
870 stdcall TlsFree(long)
871 stdcall -norelay TlsGetValue(long)
872 stdcall -norelay TlsSetValue(long ptr)
873 stdcall Toolhelp32ReadProcessMemory(long ptr ptr long ptr)
874 stdcall TransactNamedPipe(long ptr long ptr long ptr ptr)
875 stdcall TransmitCommChar(long long)
876 stdcall TryEnterCriticalSection(ptr) ntdll.RtlTryEnterCriticalSection
877 stdcall TzSpecificLocalTimeToSystemTime(ptr ptr ptr)
878 stdcall UTRegister(long str str str ptr ptr ptr)
879 stdcall UTUnRegister(long)
880 stdcall UnhandledExceptionFilter(ptr)
881 stdcall UnlockFile(long long long long long)
882 stdcall UnlockFileEx(long long long long ptr)
883 stdcall UnmapViewOfFile(ptr)
884 stdcall UnregisterConsoleIME()
885 stdcall UnregisterWait(long)
886 stdcall UnregisterWaitEx(long long)
887 stdcall UpdateResourceA(long str str long ptr long)
888 stdcall UpdateResourceW(long wstr wstr long ptr long)
889 stdcall VDMConsoleOperation(long long)
890 stdcall VDMOperationStarted(long)
891 stdcall ValidateLCType(long long ptr ptr)
892 stdcall ValidateLocale(long)
893 stdcall VerLanguageNameA(long str long)
894 stdcall VerLanguageNameW(long wstr long)
895 stdcall -ret64 VerSetConditionMask(long long long long) ntdll.VerSetConditionMask
896 stdcall VerifyConsoleIoHandle(long)
897 stdcall VerifyVersionInfoA(long long double)
898 stdcall VerifyVersionInfoW(long long double)
899 stdcall VirtualAlloc(ptr long long long)
900 stdcall VirtualAllocEx(long ptr long long long)
901 stdcall VirtualFree(ptr long long)
902 stdcall VirtualFreeEx(long ptr long long)
903 stdcall VirtualLock(ptr long)
904 stdcall VirtualProtect(ptr long long ptr)
905 stdcall VirtualProtectEx(long ptr long long ptr)
906 stdcall VirtualQuery(ptr ptr long)
907 stdcall VirtualQueryEx(long ptr ptr long)
908 stdcall VirtualUnlock(ptr long)
909 stdcall WTSGetActiveConsoleSessionId()
910 stdcall WaitCommEvent(long ptr ptr)
911 stdcall WaitForDebugEvent(ptr long)
912 stdcall WaitForMultipleObjects(long ptr long long)
913 stdcall WaitForMultipleObjectsEx(long ptr long long long)
914 stdcall WaitForSingleObject(long long)
915 stdcall WaitForSingleObjectEx(long long long)
916 stdcall WaitNamedPipeA (str long)
917 stdcall WaitNamedPipeW (wstr long)
918 stdcall WideCharToMultiByte(long long wstr long ptr long ptr ptr)
919 stdcall WinExec(str long)
920 stdcall Wow64DisableWow64FsRedirection(ptr)
921 stdcall Wow64EnableWow64FsRedirection(long)
922 stdcall Wow64RevertWow64FsRedirection(ptr)
923 stdcall WriteConsoleA(long ptr long ptr ptr)
924 stdcall WriteConsoleInputA(long ptr long ptr)
925 stdcall WriteConsoleInputVDMA(long long long long)
926 stdcall WriteConsoleInputVDMW(long long long long)
927 stdcall WriteConsoleInputW(long ptr long ptr)
928 stdcall WriteConsoleOutputA(long ptr long long ptr)
929 stdcall WriteConsoleOutputAttribute(long ptr long long ptr)
930 stdcall WriteConsoleOutputCharacterA(long ptr long long ptr)
931 stdcall WriteConsoleOutputCharacterW(long ptr long long ptr)
932 stdcall WriteConsoleOutputW(long ptr long long ptr)
933 stdcall WriteConsoleW(long ptr long ptr ptr)
934 stdcall WriteFile(long ptr long ptr ptr)
935 stdcall WriteFileEx(long ptr long ptr ptr)
936 stdcall WriteFileGather(long ptr long ptr ptr)
937 stdcall WritePrivateProfileSectionA(str str str)
938 stdcall WritePrivateProfileSectionW(wstr wstr wstr)
939 stdcall WritePrivateProfileStringA(str str str str)
940 stdcall WritePrivateProfileStringW(wstr wstr wstr wstr)
941 stdcall WritePrivateProfileStructA (str str ptr long str)
942 stdcall WritePrivateProfileStructW(wstr wstr ptr long wstr)
943 stdcall WriteProcessMemory(long ptr ptr long ptr)
944 stdcall WriteProfileSectionA(str str)
945 stdcall WriteProfileSectionW(str str)
946 stdcall WriteProfileStringA(str str str)
947 stdcall WriteProfileStringW(wstr wstr wstr)
948 stdcall WriteTapemark(ptr long long long)
949 stdcall ZombifyActCtx(ptr)
@ stdcall -arch=x86_64 __C_specific_handler() ntdll.__C_specific_handler
@ stdcall -arch=x86_64 __chkstk() ntdll.__chkstk
;@ stdcall -arch=x86_64 __misaligned_access() ntdll.__misaligned_access
950 stdcall _hread(long ptr long)
951 stdcall _hwrite(long ptr long)
952 stdcall _lclose(long)
953 stdcall _lcreat(str long)
954 stdcall _llseek(long long long)
@ stdcall -arch=x86_64 _local_unwind() ntdll._local_unwind
955 stdcall _lopen(str long)
956 stdcall _lread(long ptr long) _hread
957 stdcall _lwrite(long ptr long) _hwrite
958 stdcall lstrcat(str str) lstrcatA
959 stdcall lstrcatA(str str)
960 stdcall lstrcatW(wstr wstr)
961 stdcall lstrcmp(str str) lstrcmpA
962 stdcall lstrcmpA(str str)
963 stdcall lstrcmpW(wstr wstr)
964 stdcall lstrcmpi(str str) lstrcmpiA
965 stdcall lstrcmpiA(str str)
966 stdcall lstrcmpiW(wstr wstr)
967 stdcall lstrcpy(ptr str) lstrcpyA
968 stdcall lstrcpyA(ptr str)
969 stdcall lstrcpyW(ptr wstr)
970 stdcall lstrcpyn(ptr str long) lstrcpynA
971 stdcall lstrcpynA(ptr str long)
972 stdcall lstrcpynW(ptr wstr long)
973 stdcall lstrlen(str) lstrlenA
974 stdcall lstrlenA(str)
975 stdcall lstrlenW(wstr)
;@ stdcall -arch=x86_64 uaw_lstrcmpW(wstr wstr)
;@ stdcall -arch=x86_64 uaw_lstrcmpiW(wstr wstr)
;@ stdcall -arch=x86_64 uaw_lstrlenW(wstr)
;@ stdcall -arch=x86_64 uaw_wcschr(wstr long)
;@ stdcall -arch=x86_64 uaw_wcscpy(ptr wstr)
;@ stdcall -arch=x86_64 uaw_wcsicmp(wstr wstr)
;@ stdcall -arch=x86_64 uaw_wcslen(wstr)
;@ stdcall -arch=x86_64 uaw_wcsrchr(wstr long)


#Vista functions
@ stdcall CompareStringOrdinal(wstr long wstr long long)
@ stdcall GetCurrentPackageId(ptr ptr)
@ stdcall GetPackageFullName(long ptr ptr)
@ stdcall GetCurrentPackageFamilyName(ptr ptr)
@ stdcall GetCurrentPackageFullName(ptr ptr)
@ stub GetCurrentPackageInfo
@ stub GetDateFormatEx
@ stub GetTimeFormatEx
@ stdcall GetErrorMode()
@ stub RaiseFailFastException
@ stdcall IsThreadAFiber()
@ stdcall SetFileInformationByHandle(long long ptr long)
@ stub CopyFile2
@ stub CreateSymbolicLinkW
@ stdcall GetFileInformationByHandleEx(ptr long ptr long)
@ stdcall OpenFileById(long ptr long long ptr long)
@ stub CancelIoEx
@ stub CancelSynchronousIo
@ stub GetOverlappedResultEx
@ stub GetQueuedCompletionStatusEx
@ stub SetStdHandleEx
@ stub GetTickCount64
@ stub LoadAppInitDlls
@ stub GlobalAddAtomExA
@ stub GlobalAddAtomExW
@ stub GetConsoleScreenBufferInfoEx
@ stub SetConsoleScreenBufferInfoEx
@ stub ResolveDelayLoadedAPI
@ stub ResolveDelayLoadsFromDll
@ stub CreateFile2
@ stub GetFinalPathNameByHandleA
@ stub GetFinalPathNameByHandleW
@ stub GetVolumeInformationByHandleW
@ stub SetFileIoOverlappedRange
@ stub CreateFileTransactedA
@ stub CreateFileTransactedW
@ stub GetDurationFormatEx
@ stub GetMaximumProcessorGroupCount
@ stub GetNamedPipeClientProcessId
@ stub GetNamedPipeClientSessionId
@ stub GetFileAttributesTransactedA
@ stub GetFileAttributesTransactedW
@ stub GetFirmwareType
@ stub GetNumaAvailableMemoryNodeEx
@ stub GetNumaProcessorNodeEx
@ stub PowerClearRequest
@ stub PowerCreateRequest
@ stub PowerCreateRequestW
@ stub PowerSetRequest
@ stub AddDllDirectory
@ stub EnumResourceLanguagesExA
@ stub EnumResourceLanguagesExW
@ stub EnumResourceNamesExA
@ stub EnumResourceNamesExW
@ stub EnumResourceTypesExA
@ stub EnumResourceTypesExW
@ stub FindStringOrdinal
@ stdcall LoadStringA(ptr long ptr long) user32.LoadStringA
@ stdcall LoadStringW(ptr long ptr long) user32.LoadStringW
@ stub QueryOptionalDelayLoadedAPI
@ stub RemoveDllDirectory
@ stub SetDefaultDllDirectories
@ stub GetCalendarInfoEx
@ stub GetLocaleInfoEx
@ stdcall GetThreadPreferredUILanguages(long ptr wstr ptr) 
@ stdcall GetThreadUILanguage()
@ stub GetUserDefaultLocaleName
@ stdcall GetUserPreferredUILanguages(long ptr wstr ptr)
@ stdcall IdnToAscii(long wstr long ptr long)
@ stdcall IdnToUnicode(long wstr long ptr long)
@ stub IsValidLocaleName
@ stdcall LCMapStringEx(wstr long wstr long ptr long ptr ptr long)
@ stub LocaleNameToLCID
@ stdcall SetThreadPreferredUILanguages(long wstr ptr)
@ stub FindNLSString
@ stub FindNLSStringEx
@ stdcall GetFileMUIInfo(long wstr ptr ptr)
@ stdcall GetFileMUIPath(long wstr wstr ptr wstr ptr ptr)
@ stub GetNLSVersionEx
@ stdcall GetProcessPreferredUILanguages(long ptr wstr ptr)
@ stdcall GetSystemPreferredUILanguages(long ptr wstr ptr)
@ stdcall GetUILanguageInfo(long wstr wstr ptr ptr)
@ stub IsValidNLSVersion
@ stub ResolveLocaleName
@ stdcall SetProcessPreferredUILanguages(long wstr ptr)
@ stub EnumSystemLocalesEx
@ stub EnumCalendarInfoExEx
@ stub EnumDateFormatsExEx
@ stub EnumTimeFormatsEx
@ stub GetCurrencyFormatEx
@ stub GetNumberFormatEx
@ stub GetSystemDefaultLocaleName
@ stub LCIDToLocaleName
@ stub NlsCheckPolicy
@ stub NlsEventDataDescCreate
@ stub NlsUpdateLocale
@ stub NlsUpdateSystemLocale
@ stub NlsWriteEtwEvent
@ stub CreateFileMappingFromApp
@ stub CreateFileMappingNumaW
@ stub MapViewOfFileFromApp
@ stub PrefetchVirtualMemory
@ stub UnmapViewOfFileEx
@ stub AllocateUserPhysicalPagesNuma
@ stub GetMemoryErrorHandlingCapabilities
@ stub RegisterBadMemoryNotification
@ stub UnregisterBadMemoryNotification
@ stub VirtualAllocExNuma
@ stub GetNamedPipeClientComputerNameW
@ stub AddSIDToBoundaryDescriptor
@ stub ClosePrivateNamespace
@ stub CreateBoundaryDescriptorW
@ stub CreatePrivateNamespaceW
@ stub DeleteBoundaryDescriptor
@ stub OpenPrivateNamespaceW
@ stub GetStringScripts
@ stub IdnToNameprepUnicode
@ stub IsNormalizedString
@ stub NormalizeString
@ stub VerifyScripts
@ stub FlushProcessWriteBuffers
@ stdcall CreateProcessAsUserW(long wstr wstr ptr ptr long long ptr wstr ptr ptr)
@ stub CreateRemoteThreadEx
@ stub DeleteProcThreadAttributeList
@ stub GetCurrentProcessorNumberEx
@ stub GetCurrentThreadStackLimits
@ stub GetProcessMitigationPolicy
@ stub GetThreadIdealProcessorEx
@ stub InitializeProcThreadAttributeList
@ stdcall OpenProcessToken(ptr long ptr)
@ stdcall OpenThreadToken(ptr long long ptr)
@ stub QueryProcessAffinityUpdateMode
@ stub SetProcessAffinityUpdateMode
@ stub SetProcessMitigationPolicy
@ stub SetThreadIdealProcessorEx
@ stdcall SetThreadToken(ptr ptr)
@ stub UpdateProcThreadAttribute
@ stub IsProcessCritical
@ stub GetThreadInformation
@ stub SetThreadInformation
@ stub K32EnumPageFilesA
@ stub K32GetDeviceDriverBaseNameA
@ stub K32GetDeviceDriverFileNameA
@ stub K32GetMappedFileNameA
@ stub K32GetProcessImageFileNameA
@ stub QueryFullProcessImageNameA
@ stub K32EmptyWorkingSet
@ stub K32EnumDeviceDrivers
@ stub K32EnumPageFilesW
@ stub K32EnumProcesses
@ stub K32GetDeviceDriverBaseNameW
@ stub K32GetDeviceDriverFileNameW
@ stub K32GetMappedFileNameW
@ stub K32GetPerformanceInfo
@ stub K32GetProcessImageFileNameW
@ stub K32GetProcessMemoryInfo
@ stub K32GetWsChanges
@ stub K32GetWsChangesEx
@ stub K32InitializeProcessForWsWatch
@ stub K32QueryWorkingSet
@ stub K32QueryWorkingSetEx
@ stub QueryFullProcessImageNameW
@ stub K32EnumProcessModules
@ stub K32EnumProcessModulesEx
@ stub K32GetModuleBaseNameA
@ stub K32GetModuleBaseNameW
@ stub K32GetModuleFileNameExA
@ stub K32GetModuleFileNameExW
@ stub K32GetModuleInformation
@ stub QueryIdleProcessorCycleTime
@ stub QueryIdleProcessorCycleTimeEx
@ stub QueryProcessCycleTime
@ stub QueryThreadCycleTime
@ stub QueryUnbiasedInterruptTime
@ stub QueryActCtxSettingsW
@ stub AcquireSRWLockExclusive
@ stub AcquireSRWLockShared
@ stub CreateEventExA
@ stub CreateEventExW
@ stub CreateMutexExA
@ stub CreateMutexExW
@ stub CreateSemaphoreExW
@ stub CreateWaitableTimerExW
@ stub DeleteSynchronizationBarrier
@ stub EnterSynchronizationBarrier
@ stub InitOnceBeginInitialize
@ stdcall InitOnceComplete(ptr long ptr)
@ stdcall InitOnceExecuteOnce(ptr ptr ptr ptr)
@ stub InitOnceInitialize
@ stub InitializeConditionVariable
@ stub InitializeCriticalSectionEx
@ stub InitializeSRWLock
@ stub InitializeSynchronizationBarrier
@ stub ReleaseSRWLockExclusive
@ stub ReleaseSRWLockShared
@ stub SetWaitableTimerEx
@ stub SleepConditionVariableCS
@ stub SleepConditionVariableSRW
@ stub TryAcquireSRWLockExclusive
@ stub TryAcquireSRWLockShared
@ stub WakeAllConditionVariable
@ stub WakeConditionVariable
@ stub GetLogicalProcessorInformationEx
@ stub GetProductInfo
@ stub GetSystemTimePreciseAsFileTime
@ stub DnsHostnameToComputerNameExW
@ stub GetPhysicallyInstalledSystemMemory
@ stub InstallELAMCertificateInfo
@ stub SetComputerNameEx2W
@ stub CallbackMayRunLong
@ stub CancelThreadpoolIo
@ stub CloseThreadpool
@ stub CloseThreadpoolCleanupGroup
@ stub CloseThreadpoolCleanupGroupMembers
@ stub CloseThreadpoolIo
@ stub CloseThreadpoolTimer
@ stub CloseThreadpoolWait
@ stub CloseThreadpoolWork
@ stub CreateThreadpool
@ stub CreateThreadpoolCleanupGroup
@ stub CreateThreadpoolIo
@ stub CreateThreadpoolTimer
@ stub CreateThreadpoolWait
@ stub CreateThreadpoolWork
@ stub DisassociateCurrentThreadFromCallback
@ stub FreeLibraryWhenCallbackReturns
@ stub IsThreadpoolTimerSet
@ stub LeaveCriticalSectionWhenCallbackReturns
@ stub QueryThreadpoolStackInformation
@ stub ReleaseMutexWhenCallbackReturns
@ stub ReleaseSemaphoreWhenCallbackReturns
@ stub SetEventWhenCallbackReturns
@ stub SetThreadpoolStackInformation
@ stub SetThreadpoolThreadMaximum
@ stub SetThreadpoolThreadMinimum
@ stub SetThreadpoolTimer
@ stub SetThreadpoolWait
@ stub StartThreadpoolIo
@ stub SubmitThreadpoolWork
@ stub TrySubmitThreadpoolCallback
@ stub WaitForThreadpoolIoCallbacks
@ stub WaitForThreadpoolTimerCallbacks
@ stub WaitForThreadpoolWaitCallbacks
@ stub WaitForThreadpoolWorkCallbacks
@ stub SetThreadpoolTimerEx
@ stub SetThreadpoolWaitEx
@ stub GetDynamicTimeZoneInformation
@ stub GetTimeZoneInformationForYear
@ stub SystemTimeToTzSpecificLocalTimeEx
@ stub TzSpecificLocalTimeToSystemTimeEx
@ stub GetApplicationRecoveryCallback
@ stub GetApplicationRestartSettings
@ stub WerRegisterFile
@ stub WerRegisterMemoryBlock
@ stub WerRegisterRuntimeExceptionModule
@ stub WerUnregisterFile
@ stub WerUnregisterMemoryBlock
@ stub WerUnregisterRuntimeExceptionModule
@ stub WerpNotifyLoadStringResource
@ stub WerpNotifyUseStringResource
@ stdcall BaseSetLastNTError(long)
@ stub CheckElevation
@ stub CheckElevationEnabled
@ stub CompareCalendarDates
@ stub GetCalendarMonthsInYear
@ stub GetActiveProcessorCount
@ stdcall BaseCleanupAppcompatCache()
@ stdcall BaseInitAppcompatCache()
@ stub CreateProcessInternalWSecure
@ stub CreateVirtualBuffer
@ stub ExtendVirtualBuffer
@ stub FreeVirtualBuffer
@ stub GetNumaAvailableMemory
@ stub GetNumaProcessorMap
@ stub NumaVirtualQueryNode
@ stub QueryWin31IniFilesMappedToRegistry
@ stub SetSearchPathMode
@ stub TrimVirtualBuffer
@ stub VirtualBufferExceptionHandler
@ stub uaw_lstrcmpW
@ stub uaw_lstrcmpiW
@ stub uaw_lstrlenW
@ stub uaw_wcschr
@ stub uaw_wcscpy
@ stub uaw_wcsicmp
@ stub uaw_wcslen
@ stub uaw_wcsrchr

@ stub QuirkIsEnabled3
@ stub GetNamedPipeAttribute
@ stdcall ImpersonateNamedPipeClient(long)
@ stdcall CompareStringEx(wstr long wstr long wstr long ptr ptr long)
@ stub GetThreadErrorMode
@ stub SetThreadErrorMode
@ stub CreateSemaphoreExA
@ stub CreateWaitableTimerExA

@ stub AppPolicyGetProcessTerminationMethod
@ stub AppPolicyGetShowDeveloperDiagnostic
@ stub AppPolicyGetThreadInitializationType
@ stub AppPolicyGetWindowingModel

@ stdcall PathCchAddBackslash(wstr long)
@ stdcall PathCchAddBackslashEx(wstr long ptr ptr) 
@ stdcall PathCchCombineEx(ptr long ptr ptr long)
@ stdcall GetNumaNodeProcessorMaskEx(long ptr)
@ stdcall GetNamedPipeClientComputerNameA(ptr str long)
@ stdcall GetNamedPipeServerProcessId(ptr ptr)
@ stdcall LoadPackagedLibrary(wstr long)