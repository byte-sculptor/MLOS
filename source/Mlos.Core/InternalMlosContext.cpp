//*********************************************************************
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root
// for license information.
//
// @File: InternalMlosContext.cpp
//
// Purpose:
//      <description>
//
// Notes:
//      <special-instructions>
//
//*********************************************************************

#include "Mlos.Core.h"
#include "Mlos.Core.inl"

namespace Mlos
{
namespace Core
{
//----------------------------------------------------------------------------
// NAME: InternalMlosContextInitializer::Create
//
// PURPOSE:
//  Creates the shared memory used for the communication channel.
//
// NOTES:
//
_Must_inspect_result_
HRESULT InternalMlosContext::Create(_Inout_ AlignedInstance<InternalMlosContext>& mlosContextInstance)
{
    const size_t SharedMemorySize = 65536;

    HRESULT hr = S_OK;

    // Global shared memory region.
    //
    SharedMemoryRegionView<Internal::GlobalMemoryRegion> globalMemoryRegionView;

    // Named shared memory for Telemetry and Control Channel.
    //
    SharedMemoryMapView controlChannelMemoryMapView;
    SharedMemoryMapView feedbackChannelMemoryMapView;

    if (SUCCEEDED(hr))
    {
        hr = globalMemoryRegionView.CreateNew("Test_Mlos.GlobalMemory", SharedMemorySize);
    }

    if (SUCCEEDED(hr))
    {
        hr = controlChannelMemoryMapView.CreateNew("Test_SharedChannelMemory", SharedMemorySize);
    }

    if (SUCCEEDED(hr))
    {
        hr = feedbackChannelMemoryMapView.CreateNew("Test_FeedbackChannelMemory", SharedMemorySize);
    }

    globalMemoryRegionView.CleanupOnClose = true;
    controlChannelMemoryMapView.CleanupOnClose = true;
    feedbackChannelMemoryMapView.CleanupOnClose = true;

    if (FAILED(hr))
    {
        // Close all the shared maps if we fail to create one.
        //
        globalMemoryRegionView.Close();
        controlChannelMemoryMapView.Close();
        feedbackChannelMemoryMapView.Close();
    }

    // Create MlosContext.
    //
    mlosContextInstance.Initialize(
        std::move(globalMemoryRegionView),
        std::move(controlChannelMemoryMapView),
        std::move(feedbackChannelMemoryMapView));

    return hr;
}

//----------------------------------------------------------------------------
// NAME: InternalMlosContext::Constructor
//
// PURPOSE:
//  Creates InternalMlosContext instance.
//
// NOTES:
//
InternalMlosContext::InternalMlosContext(
    _In_ SharedMemoryRegionView<Internal::GlobalMemoryRegion> globalMemoryRegionView,
    _In_ SharedMemoryMapView&& controlChannelMemoryMapView,
    _In_ SharedMemoryMapView&& feedbackChannelMemoryMapView) noexcept
  :  MlosContext(globalMemoryRegionView.MemoryRegion(), m_controlChannel, m_controlChannel, m_feedbackChannel),
    m_globalMemoryRegionView(std::move(globalMemoryRegionView)),
    m_controlChannelMemoryMapView(std::move(controlChannelMemoryMapView)),
    m_feedbackChannelMemoryMapView(std::move(feedbackChannelMemoryMapView)),
    m_controlChannel(
        m_globalMemoryRegionView.MemoryRegion().ControlChannelSynchronization,
        m_controlChannelMemoryMapView),
    m_feedbackChannel(
        m_globalMemoryRegionView.MemoryRegion().FeedbackChannelSynchronization,
        m_feedbackChannelMemoryMapView)
{
}
}
}
