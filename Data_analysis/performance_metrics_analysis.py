df0 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_65.pkl')
df1 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_66.pkl')
df2 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_67.pkl')
df3 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_68.pkl')
df4 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_69.pkl')
df5 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_70.pkl')
df6 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_71.pkl')
df7 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_72.pkl')
df8 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_73.pkl')
df9 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_sender_74.pkl')

df_144 = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7, df8, df9]).groupby(level=0).mean()

density = pd.DataFrame({'Density':[144]*130})
df_144 = pd.concat([df_144, density], axis=1)
df_144['PDR'] = df_144['PDR'].replace(0, np.nan)

pd.to_pickle(df_144, './pickle_files/density_144/AC0_density_144_final.pkl')

d0 = pd.read_pickle('./pickle_files/density_144/AC0_density_144_final.pkl')
d1 = pd.read_pickle('./pickle_files/density_144/AC1_density_144_final.pkl')
d2 = pd.read_pickle('./pickle_files/density_144/AC2_density_144_final.pkl')
d3 = pd.read_pickle('./pickle_files/density_144/AC3_density_144_final.pkl')

ac = ['AC0', 'AC1', 'AC2', 'AC3']
frames = [d0, d1, d2, d3]
          
plt.rcParams['figure.figsize'] = [10, 6]

print ('Receiver vs PDR')
fig = plt.figure()
for i in range(len(frames)):
    plt.plot(frames[i]['Receiver Node'], frames[i]['PDR'], label=ac[i])
#plt.plot([0, 50], [0.9, 0.9])
#plt.ylim([0.5, 1.0])
plt.legend()
plt.xlabel("Receiver")
plt.ylabel("PDR")
plt.savefig('./plots/density_144_pdr.png')
plt.show()

print ('Receiver vs Average Delay')
fig = plt.figure()
for i in range(len(frames)):
    plt.plot(frames[i]['Receiver Node'], frames[i]['Average Delay'], label=ac[i])
plt.legend()
plt.xlabel("Receiver")
plt.ylabel("Average Delay")
plt.savefig('./plots/density_144_delay.png')
plt.show()

print ('Receiver vs Average PIR')
fig = plt.figure()
for i in range(len(frames)):
    plt.plot(frames[i]['Receiver Node'], frames[i]['Average PIR'], label=ac[i])
plt.legend()
plt.xlabel("Receiver")
plt.ylabel("Average PIR")
plt.savefig('./plots/density_144_pir.png')
plt.show()
