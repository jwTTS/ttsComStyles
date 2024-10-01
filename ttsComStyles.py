#%% Import packages

import plotly.graph_objects as go
import streamlit as st
import numpy as np

#%% Headings

st.header('Training The Street communication styles tool')

#%% Set lists for options

listSpeakVol = {'Low speaking volume': -2,
                ' ': -1,
                '  ': 0,
                '   ': 1,
                'High speaking volume': 2}

listConfront = {'Less confrontational': -2, 
                ' ': -1,
                '  ': 0,
                '   ': 1,
                'Strong opinions': 2}

listDecisive = {'Take time and ask for help to make decisions': -2, 
                ' ': -1,
                '  ': 0,
                '   ': 1,
                'Quick, unilateral decisions': 2}

listDominate = {'Listen and encourage': -2, 
                ' ': -1,
                '  ': 0,
                '   ': 1,
                'Dominate conversation': 2}

listGesturing = {'Less gesturing': -2, 
                 ' ': -1,
                 '  ': 0,
                 '   ': 1,
                 'More gesturing': 2}

listExpressive = {'More expressive': -2, 
                  ' ': -1,
                  '  ': 0,
                  '   ': 1,
                  'Less expressive': 2}

listFacts = {'Use feelings to make decisions': -2, 
             ' ': -1,
             '  ': 0,
             '   ': 1,
             'Use facts to make decisions': 2}

listSerious = {'Casual, personal': -2,
               ' ': -1,
               '  ': 0,
               '   ': 1,
               'Formal, serious': 2}

listInteraction = {'More interaction': -2,
                   ' ': -1,
                   '  ': 0,
                   '   ': 1,
                   'Less interaction': 2}

listStructured = {'Less structured': -2, 
                  ' ': -1,
                  '  ': 0,
                  '   ': 1,
                  'More structured': 2}

speakVol = listSpeakVol[st.select_slider('', options=listSpeakVol,
                                         label_visibility='collapsed')]
'---'
confront = listConfront[st.select_slider('', options=listConfront, 
                                         label_visibility='collapsed')]
'---'
decisive = listDecisive[st.select_slider('', options=listDecisive, 
                                         label_visibility='collapsed')]
'---'
dominate = listDominate[st.select_slider('', options=listDominate, 
                                         label_visibility='collapsed')]
'---'
gesturing = listGesturing[st.select_slider('', options=listGesturing,
                                           label_visibility='collapsed')]
'---'
expressive = listExpressive[st.select_slider('', options=listExpressive,
                                             label_visibility='collapsed')]
'---'
facts = listFacts[st.select_slider('', options=listFacts,
                                   label_visibility='collapsed')]
'---'
serious = listSerious[st.select_slider('', options=listSerious, 
                                       label_visibility='collapsed')]
'---'
interaction = listInteraction[st.select_slider('', options=listInteraction,
                                               label_visibility='collapsed')]
'---'
structured = listStructured[st.select_slider('', options=listStructured,
                                             label_visibility='collapsed')]
'---'

#%% Calculate the measures

ptVals = [expressive, facts, serious, interaction, structured]
arVals = [speakVol, confront, decisive, dominate, gesturing]

peopletask = np.mean(ptVals)
assertreflect = np.mean(arVals)

#%% Plot the chart

js = .1
plt = go.Figure()
plt.add_trace(go.Scatter(x=[peopletask], y=[assertreflect],
                         mode='markers',
                         marker=dict(color='#027D07',
                                     size=20),
                         name='Average of All Responses',
                         hovertemplate='<b>Average of All Responses</b><extra></extra>'))
plt.add_trace(go.Scatter(x=[x + np.random.uniform(-js,js) for x in arVals],
                         y=[0 + np.random.uniform(-js,js) for y in range(5)], 
                         mode='markers',
                         marker=dict(opacity=0.9,
                                     color='#8DDB98',
                                     size=8),
                         name='Task vs. People Responses',
                         hoverinfo='skip'))
plt.add_trace(go.Scatter(x=[0 + np.random.uniform(-js,js) for x in range(5)],
                         y=[y + np.random.uniform(-js,js) for y in ptVals], 
                         mode='markers',
                         marker=dict(opacity=.6,
                                     color='#31859C',
                                     size=8),
                         name='Reflective vs. Assertive Responses',
                         hoverinfo='skip'))
plt.update_xaxes(range=[-2.2, 2.2])
plt.update_yaxes(range=[-2.2, 2.2])
plt.update_layout(xaxis=dict(showgrid=False, 
                             zerolinewidth=3,
                             zeroline=True,
                             showticklabels=False),
                  yaxis=dict(showgrid=False, 
                             zerolinewidth=3,
                             zeroline=True,
                             showticklabels=False),
                  showlegend=False)

st.plotly_chart(plt)